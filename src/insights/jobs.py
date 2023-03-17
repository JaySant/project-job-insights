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

            # verifica se o job_type está presente na lista vazia,
            # (unique_job_types) se não tiver ele adc a lista.
            if job_type not in unique_job_types:
                unique_job_types.append(job_type)
        return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
