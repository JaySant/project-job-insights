from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path, newline='', encoding='utf-8') as csvfile:
        readerCsv = csv.DictReader(csvfile)
        industries_job_types = []
        for row in readerCsv:
            industry = row['industry']

            if industry and industry not in industries_job_types:
                industries_job_types.append(industry)
        return industries_job_types


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industry = []
    for job in jobs:
        if job.get('industry') == industry:
            filtered_industry.append(job)
    return filtered_industry

