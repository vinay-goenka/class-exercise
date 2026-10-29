from pydantic import BaseModel, Field

class MovieInput(BaseModel):
    title: str
    release_year: int


class MovieResponse(MovieInput):
    id: int

class CSVInfo(BaseModel):
    # TODO 1: filename (str), rows (int), columns (int),
    # column_names (list[str]), dataset_id (int)
    filename: str
    rows: int
    columns: int
    column_names: list[str]
    dataset_id: int

class ProcessingSettings(BaseModel):
    remove_duplicates: bool = True

class ProcessConfig(BaseModel):
    processing: ProcessingSettings = Field(default_factory=ProcessingSettings)
