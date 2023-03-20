from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    except_job = {"title": "Maquinista", "salary": "2000", "type": "trainee"}
    assert except_job in jobs
