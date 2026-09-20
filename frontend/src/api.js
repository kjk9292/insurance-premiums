export async function fetchInsuranceData(zip) {
    const response = await fetch(process.env.REACT_APP_API_URL + "/insurance?zip=" + zip);
    const data = await response.json();
    return data;
}