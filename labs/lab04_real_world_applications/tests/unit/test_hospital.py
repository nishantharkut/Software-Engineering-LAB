import pytest

from labs.lab04_real_world_applications.src.hospital import HospitalSystem


def patient(system, patient_id="P001"):
    system.add_patient(patient_id, "Asha Rao", "Dr. Mehta", "Cardiology")


def test_add_and_search_patient():
    system = HospitalSystem()

    created = system.add_patient("P001", "Asha Rao", "Dr. Mehta", "Cardiology")

    assert created.patient_id == "P001"
    assert system.search_patient("P001").patient_name == "Asha Rao"


def test_duplicate_patient_id_is_rejected():
    system = HospitalSystem()
    patient(system)

    with pytest.raises(ValueError, match="Duplicate patient ID"):
        patient(system)


@pytest.mark.parametrize("name", ["", "   "])
def test_empty_patient_name_is_rejected(name):
    with pytest.raises(ValueError, match="Patient name cannot be empty"):
        HospitalSystem().add_patient("P001", name, "Dr. Mehta", "Cardiology")


def test_booking_rejects_invalid_date_and_allows_doctor_report():
    system = HospitalSystem()
    patient(system)

    with pytest.raises(ValueError, match="Invalid appointment date"):
        system.book_appointment("P001", "Dr. Mehta", "31-12-2026")

    system.book_appointment("P001", "Dr. Mehta", "2026-09-01")
    assert len(system.appointments_for_doctor("Dr. Mehta")) == 1


def test_booking_cancellation_and_update_are_validated():
    system = HospitalSystem()
    patient(system)
    system.book_appointment("P001", "Dr. Mehta", "2026-09-01")

    with pytest.raises(ValueError, match="Appointment already booked"):
        system.book_appointment("P001", "Dr. Mehta", "2026-09-02")

    system.update_appointment("P001", "Dr. Kapoor", "2026-09-02")
    assert system.search_patient("P001").doctor_name == "Dr. Kapoor"
    system.cancel_appointment("P001")
    assert system.search_patient("P001").appointment_status == "Cancelled"

    with pytest.raises(ValueError, match="No appointment exists"):
        system.cancel_appointment("P001")

