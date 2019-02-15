# test the ths-test.py program
import pytest


@pytest.mark.parametrize("patient_number, expected", [
    (0, 'normal thyroid function'),
    (3, 'hypothyroidism'),
    (6, 'hypothyroidism'),
    (9, 'hyperthyroidism')])
def test_ths(patient_number, expected):
    from tsh_diagnosis import file_loader
    from tsh_diagnosis import line_splitter
    from tsh_diagnosis import extract_names
    from tsh_diagnosis import extract_age
    from tsh_diagnosis import extract_sex
    from tsh_diagnosis import extract_scores
    from tsh_diagnosis import diagnose_tsh
    from tsh_diagnosis import create_patient_dict
    from tsh_diagnosis import create_json_file
    from tsh_diagnosis import full_diagnosis

    diagnosis = full_diagnosis(patient_number)
    assert diagnosis == expected
