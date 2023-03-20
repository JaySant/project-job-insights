from typing import Union, List, Dict
from src.insights.jobs import read
import sys


def get_max_salary(path: str) -> int:
    max_salary = 0
    reader = read(path)
    for row in reader:
        # método para verificar se tem apenas digitos
        if row['max_salary'].isdigit() and int(row['max_salary']) > max_salary:
            max_salary = int(row['max_salary'])
    return max_salary


def get_min_salary(path: str) -> int:
    # essa função utiliza o valor maximo de um inteiro
    min_salary = sys.maxsize
    reader = read(path)
    for row in reader:
        if row['min_salary'].isdigit() and int(row['min_salary']) < min_salary:
            min_salary = int(row['min_salary'])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError("Chaves 'min_salary' e 'max_salary' são obrigatórias")

    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary = int(salary)
    except (ValueError, TypeError):
        raise ValueError('Valores inválidos para salário')

    if min_salary > max_salary:
        raise ValueError("'Mix_salary' não pode ser maior que 'max_salary'")

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filter_salary_range = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary_range.append(job)
        except ValueError:
            continue
        # pula o loop caso não seja numérico ou tenha valor invalidos
    return filter_salary_range
