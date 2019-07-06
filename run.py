import Simulation

"""
	Make an instance of the simulation class.
"""
sim = Simulation.Simulation()


"""
	Parse configuration variables through.
"""
sim.setConfiguration({
		"COLORS" : {
			"BLACK": (0, 0, 0),
			"WHITE": (255, 255, 255),
			"BLUE": [(51, 51, 255), (0, 0, 255), (0, 0, 204), (0, 0, 153), (0, 0, 102)],
			"RED": [(255, 51, 51), (255, 0, 0), (204, 0, 0), (153, 0, 0), (102, 0, 0)]
		},
		"WIDTH": 10,
		"HEIGHT": 10,
		"MARGIN": 1,
		"LENGTH": 70,
		"CHANCE_OF_INFECTION_RED": 0.062,
		"CHANCE_OF_INFECTION_BLUE": 0.05,
		"ROWS": 71,
		"COLUMNS": 71
	})

"""
	Run the simulation.
"""
sim.start()