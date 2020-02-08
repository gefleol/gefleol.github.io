import validator as val
import directoryparser as dir

drink_directory="/home/johan/dev/gefleol.github.io/data/drinks/"
for drink_file in dir.get_drink_files(drink_directory):
    val.validate_drink_file(drink_file)
