from .loader import Loader

class EmptyGcpJsonLoader(Loader):
	"""
	EmptyGcpJsonLoader

	Interface for loading the necessary requisites requisites
	of the gcp json and creates the json.

	Arguments
	pd_csv - pd.DataFrame, GCP csv.
	"""
	def __init__(self, pd_csv):
		self.dataframe = pd_csv
		self.labels = self.dataframe['label'].unique()
		
		self.gcp_json = {}

	def load(self):
		for label in self.labels:
			self.gcp_json[str(label)] = []
		
		return self.gcp_json
