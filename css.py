welcome = """
    QLabel
    {
        text-align: center;
        border-radius: 35px;
        background-color: rgba(255,255,255,0.2);
        color:white;
    }"""
sign_up_main_label = """
    QLabel
    {
        font: 57 28pt \"B Badr\";
        text-align: center;
        border-radius: 25px;
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 127, 255));
        color:white;
    }
    QLabel:hover
    {
        color:yellow;
    }"""
sign_up_small_labels = """
    QLabel
    {
        font: 57 28pt \"B Badr\";
        text-align: center;
        border-radius: 16px;
        background-color: qconicalgradient(cx:0.756, cy:1, angle:296.3, stop:0 rgba(170, 255, 255, 255), stop:0.931818 rgba(45, 255, 95, 255), stop:1 rgba(255, 255, 255, 255));
    }"""
line_edit_basic = """
    QLineEdit
    {
        font: 57 28pt \"B Badr\";
        text-align: center;
        border:3px solid white;
        border-radius: 15px;
        background-color: white;
        color:gray;
    }
    QLineEdit:active
    {
        color:black;
    }
    QLineEdit:hover
    {
        border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 127, 255));
    }"""
line_edit_false = """
    QLineEdit
    {
        font: 57 28pt \"B Badr\";
        text-align: center;
        border:3px solid red;
        border-radius: 15px;
        background-color: white;
        color:gray;
    }
    QLineEdit:hover
    {
        border-color: orange;
    }
    QLineEdit:active
    {
        color:black;
    }"""
line_edit_correct = """
    QLineEdit
    {
        font: 57 28pt \"B Badr\";
        text-align: center;
        border:3px solid rgb(14, 234, 14);
        border-radius: 15px;
        background-color: white;
        color:gray;
    }
    QLineEdit:active
    {
        color:black;
    }"""
button_invisible = """
    QPushButton
    {
        background-color: rgba(0, 0, 0, 0);
        color: rgba(0, 0, 0, 0);
    }"""
button_active = """
    QPushButton
    {
        background-color:qlineargradient(spread:pad, x1:0.477727, y1:1, x2:0.511, y2:0, stop:0 rgba(61, 127, 0, 255), stop:1 rgba(35, 248, 0, 255));
        color: white;
        border: 1px solid rgb(49, 183, 0);
        border-radius: 25px;
    }
    QPushButton:pressed
    {
        background-color:qlineargradient(spread:pad, x1:0.477727, y1:1, x2:0.511, y2:0, stop:0 rgba(61, 127, 0, 255), stop:1 rgba(248, 220, 0, 255));
    }
    QPushButton:hover
    {
        color: rgb(214, 214, 214);
    }"""
button_true = """
    QPushButton
    {
        background-color:rgb(0, 234, 7);
        color: black;
        border: 1px solid rgb(0, 234, 7);
        border-radius: 25px;
    }
    QPushButton:pressed
    {
        background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.119318, stop:0 rgba(16, 207, 69, 255), stop:1 rgba(196, 196, 196, 255));\n"
    }
    QPushButton:hover
    {
        color: rgb(103, 103, 103);
    }"""
button_false = """
    QPushButton
    {
        background-color: rgb(232, 0, 0);
        color: white; 
        border: 1px solid rgb(232, 0, 0);
        border-radius: 25px;
    }
    QPushButton:hover
    {
        color: rgb(103, 103, 103);
    }"""
back_button = """
    QPushButton
    {
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 127, 255));
        color: white;
        border: 1px solid rgb(0, 0, 210);
        border-radius: 30px;
    }
    QPushButton:pressed
    {
        background-color:rgb(0, 85, 255);
    }
    QPushButton:hover
    {
        color:rgb(216, 216, 216);
    }"""
login_labels = """
    QLabel
    {
        font: 57 28pt "B Badr";
        text-align: center;
        border-radius: 16px;
        background-color:rgba(0,0,0,0.1);
        color:white;
    }
    QLabel:hover
    {
        background-color:rgba(255,255,255,0.1);
    }"""
label_ehterak = """
    QLabel
    {
        font: 20 14pt "B Badr";
        color:black;
    }"""
line_edit_request_correct = """
    QLineEdit
    {
        font: 34 20pt \"B Badr\";
        text-align: center;
        border:3px solid rgb(14, 234, 14);
        border-radius: 5px;
        background-color: white;
        color:gray;
    }
    QLineEdit:active
    {
        color:black;
    }"""
line_edit_request_false = """
    QLineEdit
    {
        font: 34 20pt \"B Badr\";
        text-align: center;
        border:3px solid red;
        border-radius: 5px;
        background-color: white;
        color:gray;
    }
    QLineEdit:hover
    {
        border-color: orange;
    }
    QLineEdit:active
    {
        color:black;
    }"""
menu_button = """
    QPushButton
    {
        background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.113636, stop:0 rgba(84, 84, 84, 255), stop:1 rgba(196, 196, 196, 255));
        color: white;
        border: 1px solid rgb(153, 153, 153);
        border-radius: 10px;
    }
    QPushButton:pressed
    {
        background-color:rgba(0, 0, 0,0.5);
    }"""
menu_exit_button = """
    QPushButton
    {
        background-color:lightgray;
        color: red;
        border: 1px solid rgb(153, 153, 153);
        border-radius: 10px;
    }
    QPushButton:pressed
    {
        background-color:rgba(0, 0, 0,0.5);
    }"""
