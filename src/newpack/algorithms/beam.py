class Beam:
    def __init__(self, start_point, end_point):
        """Create a Beam object.

        Parameters
        ----------
        start_point : [x, y, z]
            Coordinates of the start point of the beam.
        end_point : [x, y, z]
            Coordinates of the end point of the beam.

        Returns
        -------
        Beam
            The Beam object.
        """

        self.start_point = start_point
        self.end_point = end_point

    def calculate_length(self):
        """Calculate the length using the start and end points"""
        dx = self.end_point[0] - self.start_point[0]
        dy = self.end_point[1] - self.start_point[1]
        dz = self.end_point[2] - self.start_point[2]
        self.length = (dx**2 + dy**2 + dz**2) ** 0.5
        return self.length

    def store_cross_section(self, cross_section):
        """Store the cross section of the beam

        Parameters
        ----------
        cross_section : str
            Cross section name to be assigned.
        """
        # Store the cross section of the beam
        self.cross_section = cross_section

    def get_cross_section(self):
        """Returns the cross section of the beam.

        Returns
        -------
        cross_section : str
            The cross section of the beam.
        """
        return self.cross_section

    def set_properties(self, E, Ix, A):
        """Set the structural properties of the beam.

        Parameters
        ----------
        E : float
            The Young's modulus of the beam.
        Ix : float
            The moment of inertia of the beam.
        A : float
            The cross-sectional area of the beam.

        Returns
        -------
        None
            Sets the structural properties of the beam.
        """
        # Set the structural properties of the beam
        self.E = E  # Young's modulus
        self.Ix = Ix  # Moment of inertia
        self.A = A  # Cross-sectional area

    def get_youngs_modulus(self):
        """Returns the Young's modulus of the beam.

        Returns
        -------
        float
            The Young's modulus of the beam.
        """
        return self.E

    def get_moment_of_inertia(self):
        """Returns the moment of inertia of the beam.

        Returns
        -------
        float
            The moment of inertia of the beam.
        """
        return self.I

    def get_cross_sectional_area(self):
        """Returns the cross-sectional area of the beam.

        Returns
        -------
        float
            The cross-sectional area of the beam.
        """
        return self.A

    def get_properties(self):
        # Return the structural properties of the beam
        return self.E, self.I, self.A
