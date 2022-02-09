export default class Car {
  constructor(brand, motor, color) {
    // Create objects
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Methods

  cloneCar() {
    return Object.assign(Object.create(Object.getPrototypeOf(this)), {
      _brand: undefined,
      _motor: undefined,
      _color: undefined,
    });
  }
}
