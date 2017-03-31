#字典6.1
alien={'color':'red','points':'5'}
print(alien['color'])
print(alien['points'])
new_points=alien['points']
print("u got "+str(new_points)+" points")
print(alien)
alien['x_position']=0
alien['y_position']=25
print(alien)
alien={}
alien['color']='red'
alien['point']=5
print(alien)

