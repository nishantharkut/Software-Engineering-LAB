"""Hospital appointment management domain logic and console application."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Patient:
    patient_id: str
    patient_name: str
    doctor_name: str
    department: str
    appointment_date: str | None = None
    appointment_status: str = "Not Booked"


def _required_text(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()


def _valid_date(value: str) -> str:
    try:
        parsed = datetime.strptime(value.strip(), "%Y-%m-%d")
    except (AttributeError, ValueError):
        raise ValueError("Invalid appointment date; use YYYY-MM-DD") from None
    return parsed.strftime("%Y-%m-%d")


class HospitalSystem:
    """In-memory hospital patient and appointment store."""

    def __init__(self):
        self._patients: dict[str, Patient] = {}

    def add_patient(
        self, patient_id: str, patient_name: str, doctor_name: str, department: str
    ) -> Patient:
        patient_id = _required_text(patient_id, "Patient ID")
        if patient_id in self._patients:
            raise ValueError("Duplicate patient ID")
        patient = Patient(
            patient_id,
            _required_text(patient_name, "Patient name"),
            _required_text(doctor_name, "Doctor name"),
            _required_text(department, "Department"),
        )
        self._patients[patient_id] = patient
        return patient

    def list_patients(self) -> list[Patient]:
        return list(self._patients.values())

    def search_patient(self, patient_id: str) -> Patient:
        try:
            return self._patients[patient_id.strip()]
        except (AttributeError, KeyError):
            raise ValueError("Patient ID not found") from None

    def book_appointment(self, patient_id: str, doctor_name: str, appointment_date: str):
        patient = self.search_patient(patient_id)
        if patient.appointment_status == "Booked":
            raise ValueError("Appointment already booked")
        patient.doctor_name = _required_text(doctor_name, "Doctor name")
        patient.appointment_date = _valid_date(appointment_date)
        patient.appointment_status = "Booked"
        return patient

    def cancel_appointment(self, patient_id: str):
        patient = self.search_patient(patient_id)
        if patient.appointment_status != "Booked":
            raise ValueError("No appointment exists")
        patient.appointment_status = "Cancelled"
        return patient

    def update_appointment(
        self, patient_id: str, doctor_name: str, appointment_date: str
    ):
        patient = self.search_patient(patient_id)
        if patient.appointment_status != "Booked":
            raise ValueError("No appointment exists")
        patient.doctor_name = _required_text(doctor_name, "Doctor name")
        patient.appointment_date = _valid_date(appointment_date)
        return patient

    def appointments_for_doctor(self, doctor_name: str) -> list[Patient]:
        doctor_name = _required_text(doctor_name, "Doctor name")
        return [
            patient
            for patient in self._patients.values()
            if patient.doctor_name.casefold() == doctor_name.casefold()
            and patient.appointment_status == "Booked"
        ]

    def appointment_report(self) -> dict[str, int]:
        patients = self._patients.values()
        return {
            "total_patients": len(self._patients),
            "booked": sum(patient.appointment_status == "Booked" for patient in patients),
            "cancelled": sum(
                patient.appointment_status == "Cancelled" for patient in self._patients.values()
            ),
            "not_booked": sum(
                patient.appointment_status == "Not Booked" for patient in self._patients.values()
            ),
        }
