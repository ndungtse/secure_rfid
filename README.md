# Secure-RFID
In this repo, I implement a security system with RFID cards and python. 

in txt folder, the python "backend" has a `tags.txt` file that has all the Card IDs that are allowed into the system.

in db folder, I want to integrate `mysql` instead of a text file.

## Structure
```txt
src
├── arduino
│   └── index.ino
└── python
    ├── audio # --- uses audio to indicate access granted   or denied
    │   ├── denied.mp3
    │   └── granted.mp3
    |── txt # will use txt file as database
    │   ├── index.py
    │   └── tags.txt
    ├── db # --- uses mysql as database
    │   ├── index.py
```

## How to run
### Arduino
1. Open `index.ino` in Arduino IDE
2. Upload to Arduino

### Python
1. Open terminal
2. `cd` into `python` folder
3. Run `pip install -r requirements.txt`
4. Open `index.py` and change the `port` variable to the port that the Arduino is connected to
5. Run `python index.py`

## How it works
1. Arduino reads the RFID card
2. Arduino sends the card ID to the python script
3. Python script checks if the card ID is in the database
4. If the card ID is in the database, the python script sends a signal to the Arduino and the user is granted access
5. If the card ID is not in the database, the python script sends a signal to the Arduino and the buser is denied access
6. Sound is played on the Arduino to indicate if the access is granted or denied

## TODO
- [ ] Add `sqlite` database
- [ ] Add `mongodb` database
- [ ] Add `qdrant` vector database
## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
- [Ndungutse Charles](https://ndungutsecharles.me)
- [Mugisha Precieux](https://mugishap.vercel.app)
- [Ineza Axelle](https://inezaxelle.me)
- [Nzambazamariya Rosine](https://gajurosine.me)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.