from flask_bcrypt import Bcrypt

# tao mot ham bam

bcrypt = Bcrypt()

password = 'hellohehe'

#luu phien ban bam

hashed_password = bcrypt.generate_password_hash(password = password)

print(hashed_password)

#kiem tra xem mat khau cua user co khop voi ham bam hay khong

bcrypt.check_password_hash(hashed_password,'wrongpass') # neu ma nguoi dung dang nhap sai mat khau, no se hien ra false


################################

from werkzeug.security import generate_password_hash,check_password_hash

hashed_password = generate_password_hash('mypass')
print(hashed_password)

check = check_password_hash(hashed_password,'mypass')
print(check)

