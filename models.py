from pynamodb.models import Model, Key, Throughput

class Camera(Model):
	table_name = 'Camera'
	year = Key(name='year', key_type='hash', attr_type='N')
	title = Key(key_type='range', attr_type='N')
	provisioned_throughput = Throughput(read=10, write=10)

class Car(Model):
	table_name = 'Car'
	id = Key(name='id', key_type='hash', attr_type='N')
	color = Key(key_type='range', attr_type='S')


if __name__ == '__main__':
	print(Camera.get_table_name())
	'''
	TESTS
	camera = Camera()
	title = camera.title.get_values()
	print(title)
	print(camera.__dict__)
	print(vars(camera))
	year = getattr(camera, 'year')
	print(camera.get_attributes())
	print(camera.get_table_name())
	print(camera.get_required_items())
	'''
	camera = Camera(year=2005, title=2)
	camera.create(year=2005, title=3)
	camera.create(year=2005, title=4)
	camera.create(year=2005, title=5)
	camera.create(year=2006, title=3)
	camera.create(year=2007, title=3)

	car = Car(id=1, color='red').create()

	camera = camera.create()
	print(camera)

	camera = Camera.get(year=2005, title=2)
	print(camera)

	cameras = Camera.query(year=2005)
	print(cameras)
	'''
	cameras = Camera.query(year='>2005')
	cameras = Camera.query(year='=>2005')
	cameras = Camera.query(year='<2005')
	cameras = Camera.query(year='<=2005')
	cameras = Camera.query(year='2005')
	cameras = Camera.query(year='>2005')
	cameras = Camera.query(year='>2005')
	cameras = Camera.query(year='>2005')
	cameras = Camera.query(year='>2005')
	'''
	#cameras = Camera.query(year='2005') BEGINS_WITH
	#cameras = Camera.query(year='>2005') BETWEEN
