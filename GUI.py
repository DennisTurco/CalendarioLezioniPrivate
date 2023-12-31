import GoogleCalendarEventsManager as gc
import webbrowser
import JSONSettings as js
import io, subprocess, sys, os

import tkinter
from tkinter import filedialog
from datetime import datetime

import Plotter
from DataEditor import DataCSV

try:
    import customtkinter
except:
    subprocess.call([sys.executable, "-m", "pip", "install", "customtkinter"])
    import customtkinter
try:
    from CTkMenuBar import *
except:
    subprocess.call([sys.executable, "-m", "pip", "install", "CTkMenuBar"])
    from CTkMenuBar import *
try:
    from CTkMessagebox import *
except:
    subprocess.call([sys.executable, "-m", "pip", "install", "CTkMessagebox"])
    from CTkMessagebox import *
try:
    from tkcalendar import *
except:
    subprocess.call([sys.executable, "-m", "pip", "install", "tkcalendar"])
    from tkcalendar import *

#?###########################################################
class NewEventsFrame(customtkinter.CTkFrame):
    
    main_class = None
    toplevel_window = None
    event_color = {"Lavender": "#7986cb", "Sage": "#33b679", "Grape": "#8e24aa", "Flamingo": "#e67c73", "Banana": "#f6bf26", "Tangerine": "#f4511e", "Peacock": "#039be5", "Graphite": "#616161", "Blueberry": "#3f51b5", "Basil": "#0b8043", "Tomato": "#d50000"}
    timezone = ['Africa/Abidjan', 'Africa/Accra', 'Africa/Algiers', 'Africa/Bissau', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/El_Aaiun', 'Africa/Juba', 'Africa/Khartoum', 'Africa/Lagos', 'Africa/Maputo', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Sao_Tome', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Asuncion', 'America/Atikokan', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Cayenne', 'America/Chicago', 'America/Chihuahua', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Fort_Nelson', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Nuuk', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Colombo', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kathmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qostanay', 'Asia/Qyzylorda', 'Asia/Riyadh', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ulaanbaatar', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faroe', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/Perth', 'Australia/Sydney', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GMT', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Wake', 'Pacific/Wallis', 'UTC']
    
    def __init__(self, parent, main_class):
        customtkinter.CTkFrame.__init__(self, parent)
        self.main_class = main_class
                
        # load images
        self.calendar_image = tkinter.PhotoImage(file='./imgs/calendar.png')
        self.google_image = tkinter.PhotoImage(file='./imgs/google.png')
        self.plus_image = tkinter.PhotoImage(file='./imgs/plus.png')
        self.list_image = tkinter.PhotoImage(file='./imgs/list.png')
        self.edit_image = tkinter.PhotoImage(file='./imgs/edit.png')
        self.folder_image = tkinter.PhotoImage(file='./imgs/folder.png')
        self.file_image = tkinter.PhotoImage(file='./imgs/file.png')
        self.chart_image = tkinter.PhotoImage(file='./imgs/chart.png')
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.title_label = customtkinter.CTkLabel(self.sidebar_frame, text="Other Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, image=self.plus_image, text="New Events", command=self.go_to_new_events_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, image=self.edit_image, text="Edit Events", command=self.go_to_edit_events_frame)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, image=self.list_image, text="Get Events List", command=self.go_to_get_events_by_title_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, image=self.chart_image, text="Graph", command=self.go_to_graph_frame)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.google_calendar_link = customtkinter.CTkButton(self.sidebar_frame, image=self.google_image, text="Google Calendar", command=lambda: webbrowser.open('https://calendar.google.com/'))
        self.google_calendar_link.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        # create main panel
        self.title_label_main = customtkinter.CTkLabel(self, text="Create New Event", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label_main.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nsew")
        
        # main entry
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, padx=(50, 50), pady=10, sticky="ew")
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.label_summary = customtkinter.CTkLabel(self.main_frame, text="Summary:")
        self.label_summary.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_summary = customtkinter.CTkEntry(self.main_frame, placeholder_text="summary")
        self.entry_summary.grid(row=0, column=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="w")
        self.label_description = customtkinter.CTkLabel(self.main_frame, text="Description:")
        self.label_description.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_description = customtkinter.CTkTextbox(self.main_frame, width=250, height=100)
        self.entry_description.grid(row=1, column=1, padx=(0, 0), pady=(10, 0), sticky="ew")
        self.label_color = customtkinter.CTkLabel(self.main_frame, text="Color:")
        self.label_color.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="e")
        self.multi_selection = customtkinter.CTkComboBox(self.main_frame, state="readonly", values=list(self.event_color.keys()), command=self.combobox_callback)
        self.multi_selection.set("Lavender")
        self.multi_selection.grid(row=2, column=1, padx=0, pady=(10, 10), sticky="w")
        self.color_preview = customtkinter.CTkCanvas(self.main_frame, width=15, height=15)
        self.color_preview.grid(row=2, column=1, sticky="w", padx=(150, 0), pady=(10, 10))
        self.color_preview.configure(bg=self.event_color.get('Lavender'))
        
        # date
        self.date_frame = customtkinter.CTkFrame(self, width=400)
        self.date_frame.grid(row=2, column=1, padx=(50, 50), pady=10, sticky="nsew")
        self.date_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.label_date_frame = customtkinter.CTkLabel(master=self.date_frame, text="Date Interval")
        self.label_date_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=10, sticky="ew")
        self.label_date_from = customtkinter.CTkLabel(self.date_frame, text="From:")
        self.label_date_from.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_date_from = customtkinter.CTkEntry(self.date_frame, placeholder_text="yyyy-mm-dd hh:mm")
        self.entry_date_from.grid(row=1, column=1, padx=0, pady=10, sticky="ew")
        self.entry_date_button = customtkinter.CTkButton(self.date_frame, text="", width=10, image=self.calendar_image, command=lambda: self.date_picker(1))
        self.entry_date_button.grid(row=1, column=2, padx=0, pady=10, sticky="w")
        self.label_date_to = customtkinter.CTkLabel(self.date_frame, text="To:")
        self.label_date_to.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_date_to = customtkinter.CTkEntry(self.date_frame, placeholder_text="yyyy-mm-dd hh:mm")
        self.entry_date_to.grid(row=2, column=1, padx=0, pady=10, sticky="ew")
        self.entry_date_button2 = customtkinter.CTkButton(self.date_frame, text="", width=10, image=self.calendar_image, command=lambda: self.date_picker(2))
        self.entry_date_button2.grid(row=2, column=2, padx=0, pady=10, sticky="w")
        self.label_timezone = customtkinter.CTkLabel(self.date_frame, text="Timezone:")
        self.label_timezone.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.timezone_selection = customtkinter.CTkComboBox(self.date_frame, state="readonly", values=list(self.timezone), command=self.combobox_callback)
        self.timezone_selection.set(self.timezone[len(self.timezone)-1])
        self.timezone_selection.grid(row=3, column=1, padx=0, pady=(10, 10), sticky="nsew")
        
        # create button
        self.create_button = customtkinter.CTkButton(self, image=self.plus_image, text="Create", command=self.create_event)
        self.create_button.grid(row=3, column=1, padx=20, pady=20)
        
        # create log textbox
        self.log_box = customtkinter.CTkTextbox(self, width=250, height=100)
        self.log_box.bind("<Key>", lambda e: "break")  # set the textbox readonly
        self.log_box.grid(row=4, column=1, columnspan=2, padx=(0, 0), pady=(20, 0), sticky="nsew")
    
    def create_event(self):
        summary = self.entry_summary.get()
        date_from = self.entry_date_from.get()
        date_to = self.entry_date_to.get()
        
        if len(summary.replace(" ", "")) == 0:
            self.main_class.write_log(self.log_box, f"Error on creating event: summary is missing")
            return
        if len(date_from.replace(" ", "")) == 0 or len(date_to.replace(" ", "")) == 0:
            self.main_class.write_log(self.log_box, f"Error on creating event: date is missing")
            return
        try:
            date_from = datetime.strptime(date_from, '%Y-%m-%d %H:%M')
            date_to = datetime.strptime(date_to, '%Y-%m-%d %H:%M')
        except ValueError:
            self.main_class.write_log(self.log_box, f"Error on creating event: date format is not correct")
        
        color_selected = self.multi_selection.get()
        color_index = 0
        for idx, color in enumerate(self.event_color.keys()):
            if color == color_selected:
                color_index = idx
                break
        try: 
            gc.GoogleCalendarEventsManager.createEvent(self.main_class.get_credentials(), summary, self.entry_description.get("0.0", tkinter.END), date_from, date_to, color_index)
            self.main_class.write_log(self.log_box, f"Event '{summary}' created succesfully!")
        except Exception as e:
            self.main_class.write_log(self.log_box, f"Exception occurred: {str(e)}")   
        
    def combobox_callback(self, color):
        self.color_preview.configure(bg=self.event_color.get(color))
        self.main_class.write_log(self.log_box, f"color '{color}' selected")
    
    def date_picker(self, type):
        self.toplevel_window = self.main_class.date_picker_window(type, self.toplevel_window, self.entry_date_from, self.entry_date_to, self.log_box)
    
    def go_to_new_events_frame(self):
        self.main_class.show_frame(NewEventsFrame)
    
    def go_to_edit_events_frame(self):
        self.main_class.show_frame(EditEventsFrame)
    
    def go_to_get_events_by_title_frame(self):
        self.main_class.show_frame(GetEventsFrame)
    
    def go_to_graph_frame(self):
        self.main_class.show_frame(GraphFrame)
#?###########################################################

#?###########################################################
class EditEventsFrame(customtkinter.CTkFrame):
    
    main_class = None
    event_color = {"Lavender": "#7986cb", "Sage": "#33b679", "Grape": "#8e24aa", "Flamingo": "#e67c73", "Banana": "#f6bf26", "Tangerine": "#f4511e", "Peacock": "#039be5", "Graphite": "#616161", "Blueberry": "#3f51b5", "Basil": "#0b8043", "Tomato": "#d50000"}
    timezone = ['Africa/Abidjan', 'Africa/Accra', 'Africa/Algiers', 'Africa/Bissau', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/El_Aaiun', 'Africa/Juba', 'Africa/Khartoum', 'Africa/Lagos', 'Africa/Maputo', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Sao_Tome', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Asuncion', 'America/Atikokan', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Cayenne', 'America/Chicago', 'America/Chihuahua', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Fort_Nelson', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Nuuk', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Colombo', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kathmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qostanay', 'Asia/Qyzylorda', 'Asia/Riyadh', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ulaanbaatar', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faroe', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/Perth', 'Australia/Sydney', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GMT', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Wake', 'Pacific/Wallis', 'UTC']
    
    def __init__(self, parent, main_class):
        customtkinter.CTkFrame.__init__(self, parent)
        self.main_class = main_class
        
        # load images
        self.calendar_image = tkinter.PhotoImage(file='./imgs/calendar.png')
        self.google_image = tkinter.PhotoImage(file='./imgs/google.png')
        self.plus_image = tkinter.PhotoImage(file='./imgs/plus.png')
        self.list_image = tkinter.PhotoImage(file='./imgs/list.png')
        self.edit_image = tkinter.PhotoImage(file='./imgs/edit.png')
        self.folder_image = tkinter.PhotoImage(file='./imgs/folder.png')
        self.file_image = tkinter.PhotoImage(file='./imgs/file.png')
        self.chart_image = tkinter.PhotoImage(file='./imgs/chart.png')
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 4), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.title_label = customtkinter.CTkLabel(self.sidebar_frame, text="Other Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, image=self.plus_image, text="New Events", command=self.go_to_new_events_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, image=self.edit_image, text="Edit Events", command=self.go_to_edit_events_frame)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, image=self.list_image, text="Get Events List", command=self.go_to_get_events_by_title_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, image=self.chart_image, text="Graph", command=self.go_to_graph_frame)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.google_calendar_link = customtkinter.CTkButton(self.sidebar_frame, image=self.google_image, text="Google Calendar", command=lambda: webbrowser.open('https://calendar.google.com/'))
        self.google_calendar_link.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        # create main panel
        self.title_label_main = customtkinter.CTkLabel(self, text="Edit Events", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label_main.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nsew")
                
        # Create a frame with a 1x2 grid
        main_frame = customtkinter.CTkFrame(self)
        main_frame.grid(row=1, column=1, padx=(50, 50), pady=10, sticky="ew")
        main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # old main values
        self.old_values_frame = customtkinter.CTkFrame(main_frame)
        self.old_values_frame.grid(row=1, column=1, padx=(50, 25), pady=10, sticky="ew")
        self.old_values_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.label_frame_old = customtkinter.CTkLabel(self.old_values_frame, text="OLD Values")
        self.label_frame_old.grid(row=0, column=0, columnspan=3, padx=0, pady=10, sticky="ew")
        self.label_summary_old = customtkinter.CTkLabel(self.old_values_frame, text="Summary:")
        self.label_summary_old.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_summary_old = customtkinter.CTkEntry(self.old_values_frame, placeholder_text="summary")
        self.entry_summary_old.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="w")
        self.label_description_old = customtkinter.CTkLabel(self.old_values_frame, text="Description:")
        self.label_description_old.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_description_old = customtkinter.CTkTextbox(self.old_values_frame, width=250, height=100)
        self.entry_description_old.grid(row=2, column=1, padx=(0, 0), pady=(10, 0), sticky="ew")
        self.label_color_old = customtkinter.CTkLabel(self.old_values_frame, text="Color:")
        self.label_color_old.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="e")
        self.multi_selection_old = customtkinter.CTkComboBox(self.old_values_frame, state="readonly", values=list(self.event_color.keys()), command=self.combobox_callback)
        self.multi_selection_old.set("Lavender")
        self.multi_selection_old.grid(row=3, column=1, padx=0, pady=(10, 10), sticky="w")
        self.color_preview_old = customtkinter.CTkCanvas(self.old_values_frame, width=15, height=15)
        self.color_preview_old.grid(row=3, column=1, sticky="w", padx=(150, 0), pady=(10, 10))
        self.color_preview_old.configure(bg=self.event_color.get('Lavender'))
        
        # new main values
        self.new_values_frame = customtkinter.CTkFrame(main_frame)
        self.new_values_frame.grid(row=1, column=2, padx=(25, 50), pady=10, sticky="ew")
        self.new_values_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.label_frame_new = customtkinter.CTkLabel(self.new_values_frame, text="NEW Values")
        self.label_frame_new.grid(row=0, column=0, columnspan=3, padx=0, pady=10, sticky="ew")
        self.label_summary_new = customtkinter.CTkLabel(self.new_values_frame, text="Summary:")
        self.label_summary_new.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_summary_new = customtkinter.CTkEntry(self.new_values_frame, placeholder_text="summary")
        self.entry_summary_new.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="w")
        self.label_description_new = customtkinter.CTkLabel(self.new_values_frame, text="Description:")
        self.label_description_new.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_description_new = customtkinter.CTkTextbox(self.new_values_frame, width=250, height=100)
        self.entry_description_new.grid(row=2, column=1, padx=(0, 0), pady=(10, 0), sticky="ew")
        self.label_color_new = customtkinter.CTkLabel(self.new_values_frame, text="Color:")
        self.label_color_new.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="e")
        self.multi_selection_new = customtkinter.CTkComboBox(self.new_values_frame, state="readonly", values=list(self.event_color.keys()), command=self.combobox_callback)
        self.multi_selection_new.set("Lavender")
        self.multi_selection_new.grid(row=3, column=1, padx=0, pady=(10, 10), sticky="w")
        self.color_preview_new = customtkinter.CTkCanvas(self.new_values_frame, width=15, height=15)
        self.color_preview_new.grid(row=3, column=1, sticky="w", padx=(150, 0), pady=(10, 10))
        self.color_preview_new.configure(bg=self.event_color.get('Lavender'))
           
        # date
        self.date_frame = customtkinter.CTkFrame(self, width=400)
        self.date_frame.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")
        self.date_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.label_date_frame = customtkinter.CTkLabel(master=self.date_frame, text="Date Interval")
        self.label_date_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=10, sticky="ew")
        self.label_date_from = customtkinter.CTkLabel(self.date_frame, text="From:")
        self.label_date_from.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_date_from = customtkinter.CTkEntry(self.date_frame, placeholder_text="yyyy-mm-dd hh:mm")
        self.entry_date_from.grid(row=1, column=1, padx=0, pady=10, sticky="ew")
        self.entry_date_button = customtkinter.CTkButton(self.date_frame, text="", width=10, image=self.calendar_image, command=lambda: self.date_picker(1))
        self.entry_date_button.grid(row=1, column=2, padx=0, pady=10, sticky="w")
        self.label_date_to = customtkinter.CTkLabel(self.date_frame, text="To:")
        self.label_date_to.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_date_to = customtkinter.CTkEntry(self.date_frame, placeholder_text="yyyy-mm-dd hh:mm")
        self.entry_date_to.grid(row=2, column=1, padx=0, pady=10, sticky="ew")
        self.entry_date_button2 = customtkinter.CTkButton(self.date_frame, text="", width=10, image=self.calendar_image, command=lambda: self.date_picker(2))
        self.entry_date_button2.grid(row=2, column=2, padx=0, pady=10, sticky="w")
        self.label_timezone = customtkinter.CTkLabel(self.date_frame, text="Timezone:")
        self.label_timezone.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.timezone_selection = customtkinter.CTkComboBox(self.date_frame, state="readonly", values=list(self.timezone), command=self.combobox_callback)
        self.timezone_selection.set(self.timezone[len(self.timezone)-1])
        self.timezone_selection.grid(row=3, column=1, padx=0, pady=(10, 10), sticky="nsew")
        
        # create button
        self.create_button = customtkinter.CTkButton(self, image=self.edit_image, text="Edit", command=self.edit_event)
        self.create_button.grid(row=3, column=1, columnspan=2, padx=20, pady=20)
        
        # create log textbox
        self.log_box = customtkinter.CTkTextbox(self, width=250, height=100)
        self.log_box.bind("<Key>", lambda e: "break")  # set the textbox readonly
        self.log_box.grid(row=4, column=1, columnspan=2, padx=(0, 0), pady=(20, 0), sticky="nsew")
    
    def edit_event(self):
        pass
    
    def combobox_callback(self, color):
        self.color_preview.configure(bg=self.event_color.get(color))
        self.main_class.write_log(self.log_box, f"color '{color}' selected")
    
    def go_to_new_events_frame(self):
        self.main_class.show_frame(NewEventsFrame)
    
    def go_to_edit_events_frame(self):
        self.main_class.show_frame(EditEventsFrame)
    
    def go_to_get_events_by_title_frame(self):
        self.main_class.show_frame(GetEventsFrame)
    
    def go_to_graph_frame(self):
        self.main_class.show_frame(GraphFrame)
#?###########################################################

#?###########################################################
class GetEventsFrame(customtkinter.CTkFrame):
    main_class = None
    toplevel_window = None
    toplevel_entry_window = None
    date_picker_window = None
    file_viewer_window = None
    data = None
    events = None
    event_color = {"Lavender": "#7986cb", "Sage": "#33b679", "Grape": "#8e24aa", "Flamingo": "#e67c73", "Banana": "#f6bf26", "Tangerine": "#f4511e", "Peacock": "#039be5", "Graphite": "#616161", "Blueberry": "#3f51b5", "Basil": "#0b8043", "Tomato": "#d50000"}
    timezone = ['Africa/Abidjan', 'Africa/Accra', 'Africa/Algiers', 'Africa/Bissau', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/El_Aaiun', 'Africa/Juba', 'Africa/Khartoum', 'Africa/Lagos', 'Africa/Maputo', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Sao_Tome', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Asuncion', 'America/Atikokan', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Cayenne', 'America/Chicago', 'America/Chihuahua', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Fort_Nelson', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Nuuk', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Colombo', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kathmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qostanay', 'Asia/Qyzylorda', 'Asia/Riyadh', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ulaanbaatar', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faroe', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/Perth', 'Australia/Sydney', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GMT', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Wake', 'Pacific/Wallis', 'UTC']
    
    def __init__(self, parent, main_class):
        customtkinter.CTkFrame.__init__(self, parent)
        self.main_class = main_class
        
        # load images
        self.calendar_image = tkinter.PhotoImage(file='./imgs/calendar.png')
        self.google_image = tkinter.PhotoImage(file='./imgs/google.png')
        self.plus_image = tkinter.PhotoImage(file='./imgs/plus.png')
        self.list_image = tkinter.PhotoImage(file='./imgs/list.png')
        self.edit_image = tkinter.PhotoImage(file='./imgs/edit.png')
        self.folder_image = tkinter.PhotoImage(file='./imgs/folder.png')
        self.file_image = tkinter.PhotoImage(file='./imgs/file.png')
        self.chart_image = tkinter.PhotoImage(file='./imgs/chart.png')
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.title_label = customtkinter.CTkLabel(self.sidebar_frame, text="Other Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, image=self.plus_image, text="New Events", command=self.go_to_new_events_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, image=self.edit_image, text="Edit Events", command=self.go_to_edit_events_frame)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, image=self.list_image, text="Get Events List", command=self.go_to_get_events_by_title_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, image=self.chart_image, text="Graph", command=self.go_to_graph_frame)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.google_calendar_link = customtkinter.CTkButton(self.sidebar_frame, image=self.google_image, text="Google Calendar", command=lambda: webbrowser.open('https://calendar.google.com/'))
        self.google_calendar_link.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        # create main panel
        self.title_label_main = customtkinter.CTkLabel(self, text="Get Events List", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label_main.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nsew")
        
        #TODO: add like mode check box
        #TODO: add option to update the previus get list with the new list
        # main entry
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, padx=(50, 50), pady=10, sticky="ew")
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.label_id = customtkinter.CTkLabel(self.main_frame, text="ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_id = customtkinter.CTkEntry(self.main_frame, placeholder_text="id")
        self.entry_id.grid(row=0, column=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="w")
        self.label_summary = customtkinter.CTkLabel(self.main_frame, text="Summary:")
        self.label_summary.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_summary = customtkinter.CTkEntry(self.main_frame, placeholder_text="summary")
        self.entry_summary.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="w")
        self.label_description = customtkinter.CTkLabel(self.main_frame, text="Description:")
        self.label_description.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="e")
        self.entry_description = customtkinter.CTkTextbox(self.main_frame, width=250, height=100)
        self.entry_description.grid(row=2, column=1, padx=(0, 0), pady=(10, 0), sticky="ew")
        self.label_color = customtkinter.CTkLabel(self.main_frame, text="Color:")
        self.label_color.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="e")
        self.multi_selection = customtkinter.CTkComboBox(self.main_frame, state="readonly", values=list(self.event_color.keys()), command=self.combobox_callback)
        self.multi_selection.set("Lavender")
        self.multi_selection.grid(row=3, column=1, padx=0, pady=(10, 10), sticky="w")
        self.color_preview = customtkinter.CTkCanvas(self.main_frame, width=15, height=15)
        self.color_preview.grid(row=3, column=1, sticky="w", padx=(150, 0), pady=(10, 10))
        self.color_preview.configure(bg=self.event_color.get('Lavender'))
        
        # date
        self.date_frame = customtkinter.CTkFrame(self, width=400)
        self.date_frame.grid(row=2, column=1, padx=(50, 50), pady=10, sticky="nsew")
        self.date_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.label_date_frame = customtkinter.CTkLabel(master=self.date_frame, text="Date Interval")
        self.label_date_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=10, sticky="ew")
        self.label_date_from = customtkinter.CTkLabel(self.date_frame, text="From:")
        self.label_date_from.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_date_from = customtkinter.CTkEntry(self.date_frame, placeholder_text="yyyy-mm-dd hh:mm")
        self.entry_date_from.grid(row=1, column=1, padx=0, pady=10, sticky="ew")
        self.entry_date_button = customtkinter.CTkButton(self.date_frame, text="", width=10, image=self.calendar_image, command=lambda: self.date_picker(1))
        self.entry_date_button.grid(row=1, column=2, padx=0, pady=10, sticky="w")
        self.label_date_to = customtkinter.CTkLabel(self.date_frame, text="To:")
        self.label_date_to.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_date_to = customtkinter.CTkEntry(self.date_frame, placeholder_text="yyyy-mm-dd hh:mm")
        self.entry_date_to.grid(row=2, column=1, padx=0, pady=10, sticky="ew")
        self.entry_date_button2 = customtkinter.CTkButton(self.date_frame, text="", width=10, image=self.calendar_image, command=lambda: self.date_picker(2))
        self.entry_date_button2.grid(row=2, column=2, padx=0, pady=10, sticky="w")
        self.label_timezone = customtkinter.CTkLabel(self.date_frame, text="Timezone:")
        self.label_timezone.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.timezone_selection = customtkinter.CTkComboBox(self.date_frame, state="readonly", values=list(self.timezone), command=self.combobox_callback)
        self.timezone_selection.set(self.timezone[len(self.timezone)-1])
        self.timezone_selection.grid(row=3, column=1, padx=0, pady=(10, 10), sticky="nsew")

        # file output
        self.file_output_frame = customtkinter.CTkFrame(self, width=400)
        self.file_output_frame.grid(row=3, column=1, padx=(50, 50), pady=10, sticky="nsew")
        self.file_output_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.title_label_file = customtkinter.CTkLabel(master=self.file_output_frame, text="Save results to file")
        self.title_label_file.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="s")
        self.file_path = customtkinter.CTkEntry(master=self.file_output_frame, placeholder_text="file path")
        self.file_path.grid(row=1, column=1, padx=0, pady=10, sticky="ew")
        self.button_file_path = customtkinter.CTkButton(self.file_output_frame, text="", width=10, image=self.folder_image, command=lambda: self.get_file_path(self.file_path))
        self.button_file_path.grid(row=1, column=2, padx=0, pady=10, sticky="w")
        self.button_open_file = customtkinter.CTkButton(master=self.file_output_frame, image=self.file_image, text="open", command=self.open_file)
        self.button_open_file.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="s")

        # get list button
        self.get_button = customtkinter.CTkButton(self, image=self.list_image, text="Get", command=self.get_events)
        self.get_button.grid(row=4, column=1, padx=20, pady=20)
        
        # create log textbox
        self.log_box = customtkinter.CTkTextbox(self, width=250, height=100)
        self.log_box.bind("<Key>", lambda e: "break")  # set the textbox readonly
        self.log_box.grid(row=5, column=1, columnspan=2, padx=(0, 0), pady=(20, 0), sticky="nsew")
    
    def get_events(self):
        self.events = None
        
        id = self.entry_id.get()
        if len(id) != 0:
            try: 
                self.events = gc.GoogleCalendarEventsManager.getEventByID(self.main_class.get_credentials(), id)
                self.events_list_viewer_window()
                self.main_class.write_log(self.log_box, f"Event obtained succesfully!")
                return
            except Exception as e:
                self.main_class.write_log(self.log_box, f"Exception occurred: {str(e)}")
                return
        
        summary = self.entry_summary.get()
        date_from = self.entry_date_from.get()
        date_to = self.entry_date_to.get()
         
        try:
            if len(date_from) != 0:
                date_from = datetime.strptime(date_from, '%Y-%m-%d %H:%M')
            if len(date_to) != 0:
                date_to = datetime.strptime(date_to, '%Y-%m-%d %H:%M')
        except ValueError:
            self.main_class.write_log(self.log_box, f"Error on creating event: date format is not correct")
        
        color_selected = self.multi_selection.get()
        color_index = 0
        for idx, color in enumerate(self.event_color.keys()):
            if color == color_selected:
                color_index = idx
                break
        try: 
            #TODO: add description and color parameter
            self.events = gc.GoogleCalendarEventsManager.getEvents(creds=self.main_class.get_credentials(), title=summary, start_date=date_from, end_date=date_to)
            if self.events == None or len(self.events) == 0:
                self.main_class.write_log(self.log_box, f"No events obtained")
                return
            
            self.events_list_viewer_window() # i have to truncate the list for performances reason
            self.main_class.write_log(self.log_box, f"{len(self.events)} Event(s) obtained succesfully!")
            # if len(self.events) > 100:
            #     self.main_class.write_log(self.log_box, f"Warning: preview is possible only for max 100 events")
        except Exception as e:
            self.main_class.write_log(self.log_box, f"Exception occurred: {str(e)}")
    
    def events_list_viewer_window(self):  
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = customtkinter.CTkToplevel()
            self.toplevel_window.title(f'{len(self.events)} Event(s) obtained')

            # Create a grid inside the toplevel window
            self.toplevel_window.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand vertically
            self.toplevel_window.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand horizontally
            self.toplevel_window.grid_columnconfigure(1, weight=1)  # Allow column 1 to expand horizontally
            
            event_list_file_viewer = customtkinter.CTkTextbox(self.toplevel_window)
            event_list_file_viewer.bind("<Key>", lambda e: "break")  # set the textbox readonly
            event_list_file_viewer.grid(row=0, column=0, columnspan=2, padx=0, pady=(0, 10), sticky="nsew")
            
            button_save = customtkinter.CTkButton(self.toplevel_window, text="Save results", command=lambda: self.get_filepath_to_save_results())
            button_save.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="nsew")
            
            button_cancel = customtkinter.CTkButton(self.toplevel_window, text="Cancel", command=lambda: self.close_top_frame())
            button_cancel.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="nsew")
             
            event_list_file_viewer.delete(1.0, tkinter.END)

            # obtain only important informations about the event
            event_dict = {}
            events_info = []
            index = 1
            for event in self.events:
                
                # somethimes the event doesn't have 'dateTime'
                try:
                    start_date = event['start']['dateTime']
                    end_date = event['end']['dateTime']
                except:
                    start_date = event['start']['date']
                    end_date = event['end']['date']
                
                event_dict = {
                    'index': index,
                    'ID': event['id'],
                    'summary': event['summary'],
                    'start': start_date,
                    'end': end_date
                }
                events_info.append(event_dict)
                index += 1 
            
            # print event after event
            for event in events_info:
                event_info_str = f"INDEX: {event['index']} | ID: {event['ID']} | SUMMARY: {event['summary']} | START: {event['start']} | END: {event['end']}\n"
                event_list_file_viewer.insert(tkinter.END, event_info_str)
    
            self.toplevel_window.attributes("-topmost", True) # focus to this windows
        else:
            self.toplevel_window.focus()  # if window exists focus it
        
        return self.toplevel_window
    
    def get_filepath_to_save_results(self):
        
        if self.file_path != None and len(self.file_path.get()) != 0:
            self.save_results_to_file() 
            return
        
        if self.toplevel_entry_window is None or not self.toplevel_entry_window.winfo_exists():
            
            self.toplevel_entry_window = customtkinter.CTkToplevel()
            self.toplevel_entry_window.title('Select a file to save the results')
            self.toplevel_entry_window.geometry("350x50")
            entry = customtkinter.CTkEntry(self.toplevel_entry_window)
            entry.grid(row=0, column=0, padx=5, pady=(10, 10), sticky="nsew")
            button_add_filepath = customtkinter.CTkButton(self.toplevel_entry_window, width=10, text="", image=self.folder_image, command=lambda: self.get_file_path(entry))
            button_add_filepath.grid(row=0, column=1, padx=5, pady=(10, 10), sticky="nsew")
            button_ok = customtkinter.CTkButton(self.toplevel_entry_window, width=10, text="Ok", command=lambda: self.save_results_to_file2(entry))
            button_ok.grid(row=0, column=2, padx=5, pady=(10, 10), sticky="nsew") 
                
            self.toplevel_entry_window.resizable(False, False)
            self.toplevel_entry_window.attributes("-topmost", True) # focus to this windows
        else:
            self.toplevel_entry_window.focus()  # if window exists focus it
        
        return self.toplevel_entry_window
    
    def save_results_to_file(self):
        try:
            # close the toplevel windows
            if self.toplevel_window: self.close_top_frame_window()
            if self.toplevel_entry_window: self.close_top_frame_entry_window()
            
            # get all from file csv
            self.data = DataCSV.loadDataFromFile(self.file_path.get(), '|')
            
            # add into data object
            counter = 0
            for event in self.events:
                
                # somethimes the event doesn't have 'dateTime'  
                try:
                    start_date = event['start']['dateTime']
                    end_date = event['end']['dateTime']
                except:
                    start_date = event['start']['date']
                    end_date = event['end']['date']
                
                added = DataCSV.addData(self.data, event['id'], data_list=(event['id'], event['summary'], start_date, end_date))
                if added:
                    counter += 1
                
            # save all into data
            DataCSV.saveDataToFile(self.data, self.file_path.get(), '|', 'utf-8')     
            
            self.main_class.write_log(self.log_box, f"{counter} event(s) added to file {self.file_path.get()}")
            
        except Exception as e:
            self.main_class.write_log(self.log_box, f"Exception occurred: {str(e)}")
            return  
    
    def save_results_to_file2(self, entry):
        self.file_path.delete("0", tkinter.END)
        self.file_path.insert("0", entry.get())
        
        self.save_results_to_file()
    
    def close_top_frame_window(self):
        self.toplevel_window.destroy()
        
    def close_top_frame_entry_window(self):
        self.toplevel_entry_window.destroy()
        
    def combobox_callback(self, color):
        self.color_preview.configure(bg=self.event_color.get(color))
        self.main_class.write_log(self.log_box, f"color '{color}' selected")
    
    def get_file_path(self, entry):
        self.main_class.get_file_path(self.log_box, entry)
    
    def set_logbox_text(self, text):
        self.log_box.delete("0.0", tkinter.END)
        self.log_box.insert("0.0", text)
    
    def open_file(self):
        self.file_viewer_window = self.main_class.file_viewer_window(self.file_viewer_window, self.file_path.get(), self.log_box)
    
    def date_picker(self, type):
        self.date_picker_window = self.main_class.date_picker_window(type, self.date_picker_window, self.entry_date_from, self.entry_date_to, self.log_box)
    
    def go_to_new_events_frame(self):
        self.main_class.show_frame(NewEventsFrame)
    
    def go_to_edit_events_frame(self):
        self.main_class.show_frame(EditEventsFrame)
    
    def go_to_get_events_by_title_frame(self):
        self.main_class.show_frame(GetEventsFrame)
        
    def go_to_graph_frame(self):
        self.main_class.show_frame(GraphFrame)
        self.main_class.update_logtext(self.log_box, GraphFrame)
#?###########################################################


#?###########################################################
class GraphFrame(customtkinter.CTkFrame):
    main_class = None
    date_picker_window = None
    file_viewer_window = None
    
    def __init__(self, parent, main_class):
        customtkinter.CTkFrame.__init__(self, parent)
        self.main_class = main_class
        
        # load images
        self.calendar_image = tkinter.PhotoImage(file='./imgs/calendar.png')
        self.google_image = tkinter.PhotoImage(file='./imgs/google.png')
        self.plus_image = tkinter.PhotoImage(file='./imgs/plus.png')
        self.list_image = tkinter.PhotoImage(file='./imgs/list.png')
        self.edit_image = tkinter.PhotoImage(file='./imgs/edit.png')
        self.folder_image = tkinter.PhotoImage(file='./imgs/folder.png')
        self.file_image = tkinter.PhotoImage(file='./imgs/file.png')
        self.chart_image = tkinter.PhotoImage(file='./imgs/chart.png')
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.title_label = customtkinter.CTkLabel(self.sidebar_frame, text="Other Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, image=self.plus_image, text="New Events", command=self.go_to_new_events_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, image=self.edit_image, text="Edit Events", command=self.go_to_edit_events_frame)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, image=self.list_image, text="Get Events List", command=self.go_to_get_events_by_title_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, image=self.chart_image, text="Graph", command=self.go_to_graph_frame)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.google_calendar_link = customtkinter.CTkButton(self.sidebar_frame, image=self.google_image, text="Google Calendar", command=lambda: webbrowser.open('https://calendar.google.com/'))
        self.google_calendar_link.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        # create main panel
        self.title_label_main = customtkinter.CTkLabel(self, text="Create Graph", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label_main.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nsew")
        
        # file output
        self.file_output_frame = customtkinter.CTkFrame(self, width=400)
        self.file_output_frame.grid(row=1, column=1, padx=(50, 50), pady=10, sticky="nsew")
        self.file_output_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.file_output_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.file_path = customtkinter.CTkEntry(master=self.file_output_frame, placeholder_text="file path")
        self.file_path.grid(row=1, column=1, padx=0, pady=10, sticky="ew")
        self.button_file_path = customtkinter.CTkButton(self.file_output_frame, text="", width=10, image=self.folder_image, command=self.get_file_path)
        self.button_file_path.grid(row=1, column=2, padx=0, pady=10, sticky="w")
        self.button_open_file = customtkinter.CTkButton(master=self.file_output_frame, image=self.file_image, text="open", command=self.open_file)
        self.button_open_file.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="s")

        # Generate Graph Button
        self.get_button = customtkinter.CTkButton(self, command=self.generate_graph, image=self.chart_image, text="Generate")
        self.get_button.grid(row=4, column=1, padx=20, pady=20)
        
        # create log textbox
        self.log_box = customtkinter.CTkTextbox(self, width=250, height=100)
        self.log_box.bind("<Key>", lambda e: "break")  # set the textbox readonly
        self.log_box.grid(row=5, column=1, columnspan=2, padx=(0, 0), pady=(20, 0), sticky="nsew")
    
    def combobox_callback(self, color):
        self.color_preview.configure(bg=self.event_color.get(color))
        self.main_class.write_log(self.log_box, f"color '{color}' selected")
    
    def get_file_path(self):
        file_path = filedialog.askopenfilename(title="Select file where do you want to save data", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        self.file_path.delete("0", tkinter.END)
        self.file_path.insert("0", file_path)
        self.main_class.write_log(self.log_box, f"file '{file_path}' selected")
    
    def set_logbox_text(self, text):
        self.log_box.delete("0.0", tkinter.END)
        self.log_box.insert("0.0", text)
    
    def open_file(self):
        self.file_viewer_window = self.main_class.file_viewer_window(self.file_viewer_window, self.file_path.get(), self.log_box)
    
    def date_picker(self, type):
        self.date_picker_window = self.main_class.date_picker_window(type, self.date_picker_window, self.entry_date_from, self.entry_date_to, self.log_box)
    
    def generate_graph(self):
        if self.main_class.check_file_path_errors(self.log_box, self.file_path.get()): return  
        
        try:
            self.main_class.write_log(self.log_box, "Generating chart")
            data = Plotter.Plotter.loadData(self.file_path.get())
            Plotter.Plotter.graph(data)
        except Exception as e:
            self.main_class.write_log(self.log_box, f"Exception occurred: {str(e)}")
    
    def go_to_new_events_frame(self):
        self.main_class.show_frame(NewEventsFrame)
    
    def go_to_edit_events_frame(self):
        self.main_class.show_frame(EditEventsFrame)
    
    def go_to_get_events_by_title_frame(self):
        self.main_class.show_frame(GetEventsFrame)
        
    def go_to_graph_frame(self):
        self.main_class.show_frame(GraphFrame)
#?###########################################################

#?###########################################################
class MainFrame(customtkinter.CTkFrame):
    
    main_class = None
    
    def __init__(self, parent, main_class):
        customtkinter.CTkFrame.__init__(self, parent)
        self.main_class = main_class
        
        # load images
        calendar_image = tkinter.PhotoImage(file='./imgs/calendar.png')
        google_image = tkinter.PhotoImage(file='./imgs/google.png')
        plus_image = tkinter.PhotoImage(file='./imgs/plus.png')
        list_image = tkinter.PhotoImage(file='./imgs/list.png')
        edit_image = tkinter.PhotoImage(file='./imgs/edit.png')
        folder_image = tkinter.PhotoImage(file='./imgs/folder.png')
        file_image = tkinter.PhotoImage(file='./imgs/file.png')
        chart_image = tkinter.PhotoImage(file='./imgs/chart.png')
        
        # main
        customtkinter.CTkLabel(self, text="Choose the action", fg_color="transparent", font=("Arial", 32)).pack(padx=20, pady=20)
        customtkinter.CTkButton(master=self, image=plus_image, text="New Events", command=self.go_to_new_events_frame).pack(padx=20, pady=10, anchor='center')
        customtkinter.CTkButton(master=self, image=edit_image, text="Edit Events", command=self.go_to_edit_events_frame).pack(padx=20, pady=10, anchor='center')
        customtkinter.CTkButton(master=self, image=list_image, text="Get Events", command=self.go_to_get_events_by_title_frame).pack(padx=20, pady=10, anchor='center')
        customtkinter.CTkButton(master=self, image=chart_image, text="Graph", command=self.go_to_graph_frame).pack(padx=20, pady=10, anchor='center')
    
    def go_to_new_events_frame(self):
        self.main_class.show_frame(NewEventsFrame)
    
    def go_to_edit_events_frame(self):
        self.main_class.show_frame(EditEventsFrame)
    
    def go_to_get_events_by_title_frame(self):
        self.main_class.show_frame(GetEventsFrame)
        
    def go_to_graph_frame(self):
        self.main_class.show_frame(GraphFrame)
#?###########################################################

#?###########################################################   
class SetupFrame(customtkinter.CTkFrame):
    width = 900
    height = 600
    main_class = None
    
    def __init__(self, parent, main_class):
        customtkinter.CTkFrame.__init__(self, parent)
        self.main_class = main_class
        
        # text title
        label = customtkinter.CTkLabel(self, text="Set Credentials", fg_color="transparent", font=("Arial", 32))
        label.pack(padx=20, pady=20)
        
        # buttons action
        button = customtkinter.CTkButton(master=self, text="Google Calendar", width=140, height=50, command=lambda: webbrowser.open('https://calendar.google.com/'))
        button.pack(padx=20, pady=10)
        button1 = customtkinter.CTkButton(master=self, text="Tutorial Setup", width=140, height=50, command=lambda: webbrowser.open('https://developers.google.com/workspace/guides/get-started'))
        button1.pack(padx=20, pady=10)
        button2 = customtkinter.CTkButton(master=self, text="First Setup", width=140, height=50, command=lambda: self.setCredentialsPath())
        button2.pack(padx=20, pady=10)
    
    def setCredentialsPath(self):
        # get response from dialog
        dialog = customtkinter.CTkInputDialog(title="New Credentials", text="Insert credentials path")
        credentials_path = dialog.get_input()
        token_path = credentials_path.rsplit("\\", 1)[0] + "\\" + "token.json"
        
        # get credentials
        credentials = gc.GoogleCalendarEventsManager.connectionSetup(credentials_path, gc.GoogleCalendarEventsManager.SCOPE, token_path)
        
        # response message box
        if credentials is not None:
            CTkMessagebox(message="Credentials setted succeffully", icon="check", option_1="Ok")
            
            # set credentials values to main class
            self.main_class.set_credentials(credentials, credentials_path, token_path)
            
            self.main_class.show_frame(MainFrame)
        else:
            msg = CTkMessagebox(title="Credentials error", message="Do you wish to retry?", icon="cancel", option_1="No", option_2="Yes")
            response = msg.get()
            if response=="Yes":
                self.setCredentialsPath()
#?###########################################################

#*###########################################################
class App(): 
    root = None
    credentials_path = None
    token_path = None
    credentials = None
    
    log_text = None
    
    app_width = 1100
    app_height = 900
    
    def __init__(self):
        root = customtkinter.CTk()
        self.root = root
        
        
        # self.init_window()
        # self.init_menu()
        # self.page_controller()
        
        # self.root.mainloop()
        
        # return 
        #TODO: solo per test, questo sotto va abilitato
        
        # read data from json to get path from last session
        listRes = js.SJONSettings.ReadFromJSON()
        if listRes != None:
            self.credentials_path = listRes["CredentialsPath"]
            self.token_path = listRes["TokenPath"]
            self.credentials = gc.GoogleCalendarEventsManager.connectionSetup(self.credentials_path, gc.GoogleCalendarEventsManager.SCOPE, self.token_path)
            
        self.init_window()
        self.init_menu()
        self.page_controller()
        
        self.root.mainloop()
        
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def update_logtext(self, logbox, next_frame):
        next_frame.set_logbox_text(text=logbox.get("0.0", tkinter.END))
    
    def init_window(self):
        # configure window
        self.root.iconbitmap('./imgs/icon.ico')
        self.root.title("Google Calendar Events Manager")
        self.centerWindow()
        self.root.minsize(300, 300)
    
    def init_menu(self):
        menu = CTkMenuBar(self.root)
        button_1 = menu.add_cascade("File")
        button_2 = menu.add_cascade("Edit")
        button_3 = menu.add_cascade("Settings")
        button_4 = menu.add_cascade("About")

        dropdown1 = CustomDropdownMenu(widget=button_1)
        dropdown1.add_option(option="New Credentials", command=lambda: self.setCredentialsPath())
        dropdown1.add_option(option="Open")
        dropdown1.add_option(option="Save")
        dropdown1.add_option(option="Exit", command=lambda: exit())

        dropdown1.add_separator()

        dropdown2 = CustomDropdownMenu(widget=button_2)
        dropdown2.add_option(option="Cut")
        dropdown2.add_option(option="Copy")
        dropdown2.add_option(option="Paste")

        dropdown3 = CustomDropdownMenu(widget=button_3)
        dropdown3.add_option(option="Update")
        
        sub_menu2 = dropdown3.add_submenu("Appearance")
        sub_menu2.add_option(option="System", command=lambda: customtkinter.set_appearance_mode("System"))
        sub_menu2.add_option(option="Dark", command=lambda: customtkinter.set_appearance_mode("dark"))
        sub_menu2.add_option(option="Light", command=lambda: customtkinter.set_appearance_mode("light"))

        dropdown4 = CustomDropdownMenu(widget=button_4)
        dropdown4.add_option(option="Share")
    
    def centerWindow(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width / 2) - (self.app_width / 2) 
        y = (screen_height / 2) - (self.app_height / 2) 
        
        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')
    
    def page_controller(self):
        # creating a container
        container = customtkinter.CTkFrame(self.root) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)        

        # initializing frames to an empty array
        self.frames = {} 

        # iterating through a tuple consisting of the different page layouts
        for F in (SetupFrame, MainFrame, NewEventsFrame, EditEventsFrame, GetEventsFrame, GraphFrame):

            frame = F(container, self)

            # initializing frame of that object from pages for loop
            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew")
        
        self.show_frame(MainFrame)
        
        #return
        #TODO: solo per test, questo sotto va abilitato
        if self.credentials is None or self.credentials_path is None:
            self.show_frame(SetupFrame)
        else:
            self.show_frame(MainFrame)
    
    def set_credentials(self, credentials, credentials_path, token_path):
        self.credentials = credentials
        self.credentials_path = credentials_path
        self.token_path = token_path
        js.SJONSettings.WriteToJSON(self.credentials_path, self.token_path)
    
    def date_picker_window(self, type, toplevel_window, entry_date_from, entry_date_to, log_box):
        if toplevel_window is None or not toplevel_window.winfo_exists():
            toplevel_window = customtkinter.CTkToplevel() # create window if its None or destroyed
            calendar = Calendar(toplevel_window)
            calendar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew") 
            hours = customtkinter.CTkLabel(toplevel_window, text="hours:")
            hours.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            hours = customtkinter.CTkEntry(toplevel_window, placeholder_text="hh")
            hours.grid(row=1, column=0, padx=(70, 0), pady=10, sticky="w")
            minutes = customtkinter.CTkLabel(toplevel_window, text="minutes: ")
            minutes.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            minutes = customtkinter.CTkEntry(toplevel_window, placeholder_text="mm")
            minutes.grid(row=2, column=0, padx=(70, 0), pady=10, sticky="w")
                
            if type == 1:
                toplevel_window.title("Date From")
                confirm_button = customtkinter.CTkButton(toplevel_window, text="Confirm", command=lambda: self.get_date(1, toplevel_window, entry_date_from, entry_date_to, log_box, calendar, hours, minutes))
            elif type == 2:
                toplevel_window.title("Date To")
                confirm_button = customtkinter.CTkButton(toplevel_window, text="Confirm", command=lambda: self.get_date(2, toplevel_window, entry_date_from, entry_date_to, log_box, calendar, hours, minutes))
            else:
                Exception("type option doesn't exists")
            
            confirm_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew") 
            
            toplevel_window.attributes("-topmost", True) # focus to this windows
            toplevel_window.resizable(False, False)
        else:
            toplevel_window.focus()  # if window exists focus it
        
        return toplevel_window
    
    def get_date(self, type, toplevel_window, entry_date_from, entry_date_to, log_box, calendar, hours, minutes):
        date = calendar.get_date() # get the date from the calendar
        
        try:
            if len(hours.get()) == 0: hour = 0
            else: hour = int(hours.get())
            if len(minutes.get()) == 0: minute = 0
            else: minute =  int(minutes.get())
    
            if hour > 23 or hour < 0 or minute > 59 or minute < 0: return
        except ValueError:
            return
        
        # Format the datetime object as a string in "%Y-%m-%d %H:%M" format
        date = datetime.strptime(date, "%m/%d/%y")  
        full_date = datetime(date.year, date.month, date.day, hour, minute)
        full_date_str = full_date.strftime("%Y-%m-%d %H:%M")  
        
        if type == 1:
            self.write_log(log_box, "Date Selected From: " + full_date_str)
            entry_date_from.delete("0", tkinter.END)
            entry_date_from.insert("0", full_date_str)
        elif type == 2:
            self.write_log(log_box, "Date Selected To: " + full_date_str)
            entry_date_to.delete("0", tkinter.END)
            entry_date_to.insert("0", full_date_str)
        else:
            Exception("type option doesn't exists")
        
        toplevel_window.destroy() 
    
    def get_file_path(self, logbox, entry):
        file_path = filedialog.askopenfilename(title="Select file where do you want to save data", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        entry.delete("0", tkinter.END)
        entry.insert("0", file_path)
        self.write_log(logbox, f"file '{file_path}' selected")
        return file_path
    
    def file_viewer_window(self, toplevel_window, filepath, log_box):
        
        if self.check_file_path_errors(log_box, filepath): return
        
        if toplevel_window is None or not toplevel_window.winfo_exists():
            toplevel_window = customtkinter.CTkToplevel() # create window if its None or destroyed
            toplevel_window.title(filepath)
            file_viewer = customtkinter.CTkTextbox(toplevel_window)
            file_viewer.bind("<Key>", lambda e: "break")  # set the textbox readonly
            file_viewer.pack(fill=tkinter.BOTH, expand=True)   
            
            #insert text into box
            with open(filepath, 'r', encoding='utf-8') as file:
                file_content = file.read()
                file_viewer.delete(1.0, tkinter.END)
                file_viewer.insert(tkinter.END, file_content)
        
            toplevel_window.attributes("-topmost", True) # focus to this windows
            self.write_log(log_box, f"file '{filepath}' opened")
        else:
            toplevel_window.focus()  # if window exists focus it
        
        return toplevel_window
    
    def check_file_path_errors(self, log_box, filepath):
        if filepath is None or len(filepath) == 0:
            self.write_log(log_box, f"ERROR: file path is missing")
            return True
        
        if not os.path.exists(filepath): 
            self.write_log(log_box, f"ERROR: file '{filepath}' doesn't found")
            return True
    
    def write_log(self, log_box, message):
        log_box.insert("0.0", "\n" + str(datetime.now()) + ": " + message)

    def get_credentials(self):
        return self.credentials
    
#*###########################################################

if __name__ == "__main__":
    app = App()