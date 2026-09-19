export async function fetchInsuranceData(zip) {
    const response = await fetch("http://localhost:8000/insurance?zip=" + zip);
    const data = await response.json();
    return data;
}