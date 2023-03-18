from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, newline='') as csvfile:
        readerCsv = csv.DictReader(csvfile)
        data = []
        for row in readerCsv:
            data.append(row)
        return data


def get_unique_job_types(path: str) -> List[str]:
    with open(path, newline='') as csvfile:
        readerCsv = csv.DictReader(csvfile)
        unique_job_types = []
        for row in readerCsv:
            job_type = row['job_type']

# verifica se o job_type está presente na lista vazia se não tiver adc a lista.
            if job_type not in unique_job_types:
                unique_job_types.append(job_type)
        return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job.get('job_type') == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
