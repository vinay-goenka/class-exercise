import logging

logger = logging.getLogger(__name__)

class DataStorage:
    def __init__(self):
        self.datasets = {}
        self.counter = 0

    def save_data(self, df, filename):
        self.counter += 1
        dataset_id = self.counter

        # TODO 1: Store the following dictionary in self.datasets
        # using dataset_id as the key and the dictionary as the value:
        # {"filename": filename, "data": df.copy()}
        self.datasets[dataset_id] = {"filename": filename, "data": df.copy()}

        logger.debug(f"Stored dataset: id={dataset_id}, rows={len(df)}")
        return dataset_id

    def get_data(self, dataset_id):
        item = self.datasets.get(dataset_id)
        if item is None:
            logger.debug(f"Dataset not found: id={dataset_id}")
            return None
        logger.debug(f"Retrieved dataset: id={dataset_id}")

        # TODO 2: Return a copy of the DataFrame from item
        return item["data"].copy()

        
