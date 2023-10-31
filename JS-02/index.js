const isSufficientFuel = (distance, literPerKm, fuelLeft) => {
    return fuelLeft / literPerKm >= distance;
}