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
	Key logical operators:
	cameras = Camera.query(year='2005') # EQ
	cameras = Camera.query(year__equal_to='2005') # 
	cameras = Camera.query(year='>2005') # GT
	cameras = Camera.query(year__gt='2005') # 
	cameras = Camera.query(year='=>2005') # GTE
	cameras = Camera.query(year__gte='2005') # 
	cameras = Camera.query(year='<2005') # LT
	cameras = Camera.query(year__lt='2005') # 
	cameras = Camera.query(year='<=2005') # LTE
	cameras = Camera.query(year__lte='2005') # 
	cameras = Camera.query(year=('2005', '2007')) # between
	cameras = Camera.query(year__between=('2005', '2007')) #
	cameras = Camera.query(year__between='2005, 2007') #
	cameras = Camera.query(year__begins_with='20') # begins_with

	Attribute logical operators:
	cameras = Camera.query(title='2005') # EQ
	cameras = Camera.query(title__equal_to='2005') # 
	cameras = Camera.query(title='>2005') # GT
	cameras = Camera.query(title__gt='2005') # 
	cameras = Camera.query(title='=>2005') # GTE
	cameras = Camera.query(title__gte='2005') # 
	cameras = Camera.query(title='<2005') # LT
	cameras = Camera.query(title__lt='2005') # 
	cameras = Camera.query(title='<=2005') # LTE
	cameras = Camera.query(title__lte='2005') # 
	cameras = Camera.query(title=('2005', '2007')) # between
	cameras = Camera.query(title__between=('2005', '2007')) #
	cameras = Camera.query(title='2005, 2007') #
	cameras = Camera.query(title__begins_with='20') # begins_with
	cameras = Camera.query(title__attribute_type='2005') # attribute_type
	cameras = Camera.query(title__contains='2005') # contains
	cameras = Camera.query(title__exists='2005') # exists
	cameras = Camera.query(title_is_in=['2005']) # is_in, :type param: `list`
	cameras = Camera.query(title__!='2005') # ne | <> => not equal to. 
	cameras = Camera.query(title__not_equal_to='2005') # ne | <> => not equal to. 
	cameras = Camera.query(title__net='2005') # ne | <> => not equal to. 
	cameras = Camera.query(title__not_exists='2005') # not_exists
	cameras = Camera.query(title__ne='2005') # ne | <> => not equal to. 
	cameras = Camera.query(size(year)<>='2010') # size => size(Brand) <= :v_sub
	'''

