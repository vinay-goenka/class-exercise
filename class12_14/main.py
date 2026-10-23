#main.py
from fastapi import FastAPI, Query, File, UploadFile
import logging
from class12_14.src.models import CSVInfo, MovieInput
from class12_14.src import MovieResponse
from class12_14.src.storage import DataStorage
from pathlib import Path

app = FastAPI(title="Movie API")

storage = DataStorage()

@app.get("/health")
def health_check():
    return {"status": "ok"}

#a path parameter identifies a resource (movie) to retrieve
@app.get("/demo/movies/{movie_id}")
def demo_get_movie(movie_id: int): #type annotation: it declares the expected type, int
    return {"requested_id": movie_id}


#a query parameter adjusts a request
@app.get("/demo/movies")
def demo_list_movies(limit: int = Query(default=2, ge=1)):
    #The default is 2 when limit is omitted in the query.
    # ge=1 means greater than or equal to one.
    return {"requested_limit": limit}

demo_movie_examples = []

@app.post("/demo/movie-examples", response_model=MovieResponse)
def demo_add_movie_example(movie:MovieInput):
    movie_id = len(demo_movie_examples) + 1
    record = movie.model_dump()
    record["id"] = movie_id
    demo_movie_examples.append(record)
    return record

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

movies = {
    1: {"id": 1, "title": "Movie A", "release_year": 2020},
    2: {"id": 2, "title": "Movie B", "release_year": 2021},
}

@app.get("/movies", response_model=list[MovieResponse])
def list_movies(limit: int = Query(default=2, ge=1)):
    # TODO 1: return up to limit movies as a list.
    # Log the number returned at INFO.
    # hint: movies is a dictionary whose values are movie records.
    movie_list = list(movies.values())[:limit]
    logger.info(f"Returning {len(movie_list)} movies")
    return movie_list


@app.post("/movies", response_model=MovieResponse)
def add_movie(movie: MovieInput):
    # TODO 2: 
    # Convert movie to a dictionary, add the new ID, and store it.
    # Log the new ID at INFO and return the stored record.
    movie_id = len(movies) + 1
    record = movie.model_dump()
    record["id"] = movie_id
    movies[movie_id] = record
    logger.info(f"Added movie with ID {movie_id}")
    return record

@app.post("/demo/inspect-csv")
async def demo_inspect_csv(file: UploadFile = File(...)):
    # ... in File(...) means the upload is required.
    contents = await file.read() # reads as bytes e.g. b"title,year\nMovie A,2020\n"
    return {"filename": file.filename,"size_bytes": len(contents)}



@app.post("/inspect-csv", response_model=CSVInfo)
async def inspect_csv(file: UploadFile = File(...)):
    # TODO 2: check the filename extension using pathlib.
    # Reject non-CSV files with status 400 and log a WARNING.
    path = Path(file.filename)
    if path.suffix.lower() != ".csv":
        logger.warning(f"Rejected non-CSV file: {file.filename}")
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Only CSV files are accepted.")

    # TODO 3: await the file contents and parse the CSV.
    # Catch expected parsing/decoding errors (e.g. EmptyDataError,ParserError, UnicodeDecodeError) and raise HTTPException
    # with status_code=400.
    import pandas as pd
    try:
        contents = await file.read()
        from io import BytesIO
        df = pd.read_csv(BytesIO(contents))
    except (pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeDecodeError) as e:
        logger.warning(f"Failed to parse CSV file: {file.filename}, error: {e}")
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Failed to parse CSV file.")

    # TODO 4: save the DataFrame with storage.save_data().
    # Log the dataset ID, filename at INFO.
    # Return a CSVInfo object with the ID, filename, shape, and column names.
    dataset_id = storage.save_data(df, file.filename)
    logger.info(f"Saved dataset: id={dataset_id}, filename={file.filename}")
    return CSVInfo(
        filename=file.filename,
        rows=df.shape[0],
        columns=df.shape[1],
        column_names=df.columns.tolist(),
        dataset_id=dataset_id
    )

@app.get("/datasets/{dataset_id}/shape")
def get_dataset_shape(dataset_id: int):
    # TODO 5: get the DataFrame using storage.get_data().
    # If it is missing, log a WARNING and raise HTTPException with status 404.
    # Otherwise, log successful retrieval at INFO.
    # Return a dictionary with dataset_id, rows, and columns.
    df = storage.get_data(dataset_id)
    if df is None:
        logger.warning(f"Dataset not found: id={dataset_id}")
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Dataset not found.")
    logger.info(f"Retrieved dataset: id={dataset_id}")
    return {
        "dataset_id": dataset_id,
        "rows": df.shape[0],
        "columns": df.shape[1]
    }

