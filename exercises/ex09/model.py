"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730482280"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Calculates distance between two Point objects."""
        delta_x: float = self.x - other.x
        delta_y: float = self.y - other.y
        distance: float = sqrt(delta_x**2 + delta_y**2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassigns a cell's location and sickness parameters."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness == constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Infects the cell."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """Immunizes a cell."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self) -> bool:
        """Returns if a cell is vulnerable to disease."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Return if a cell is sick or not."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def is_immune(self) -> None:
        """Checks if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def contact_with(self, other_cell: Cell) -> None:
        """Infects a cell if it is in contact with an infected cell."""
        if self.is_infected() or other_cell.is_infected():
            if self.is_infected() and other_cell.is_vulnerable():
                other_cell.contract_disease()
            elif other_cell.is_infected() and self.is_vulnerable():
                self.contract_disease()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "firebrick"
        elif self.is_immune():
            return "cornflower blue"


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_cells >= cells or infected_cells <= 0:
            raise ValueError("Invalid number of infected cells!")
        if immune_cells > cells or immune_cells < 0:
            raise ValueError("Invalid number of immune cells!")
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if len(self.population) < infected_cells:
                cell.contract_disease()
            if (len(self.population) >= infected_cells) and (len(self.population) < infected_cells + immune_cells):
                cell.immunize()
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def check_contacts(self) -> None:
        """Checks if two cells are in contact."""
        i: int = 0
        while i < len(self.population):
            i_loop: int = 0
            while i_loop < len(self.population):
                if not i <= i_loop:
                    point_primary: Point = self.population[i].location
                    point_secondary: Point = self.population[i_loop].location
                    distance: float = point_primary.distance(point_secondary)
                    if distance < constants.CELL_RADIUS:
                        self.population[i].contact_with(self.population[i_loop])
                i_loop += 1
            i += 1

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        quantity_infected: int = 0
        for cell in self.population:
            if cell.is_infected():
                quantity_infected += 1
        if quantity_infected > 0:
            return False
        else:
            return True