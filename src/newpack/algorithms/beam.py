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
        """Calculate the length using the start and end points
        """
        self.length = ((self.end_point[0] - self.start_point[0])**2 + (self.end_point[1] - self.start_point[1])**2 + (self.end_point[2] - self.start_point[2])**2)**0.5
        return self.length

    def store_cross_section(self, cross_section):
        """Store the cross section of the beam

        Parameters
        ----------
        cross_section : str
            Cross section Name
        """
        # Store the cross section of the beam
        self.cross_section = cross_section

    def get_cross_section(self):
        # Return the stored cross section of the beam
        return self.cross_section

    def set_properties(self, E, I, A):
        # Set the structural properties of the beam
        self.E = E  # Young's modulus
        self.I = I  # Moment of inertia
        self.A = A  # Cross-sectional area

    def get_properties(self):
        # Return the structural properties of the beam
        return self.E, self.I, self.A
