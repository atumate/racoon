import db

def resp_get_targets():
	for row in db.get_targets():
		print(row)
	return

def resp_add_target(target_to_add):
	added_id=db.add_target(target_to_add)
	if added_id == -1:
		print('Error! Maybe duplicated.')
	else:
		print('OK!')
		print(db.get_target(added_id).fetchone())
	return

def resp_rm_target(id):
	row=db.get_target(id).fetchone()
	rows=db.rm_target(id)
	if rows == -1:
		print('Error! See log.txt for details.')
	else:
		print('OK! '+str(rows)+' row removed!')
		print(row)
	return


# resp_add_target('vvvddde')

resp_get_targets()
resp_rm_target(50)


