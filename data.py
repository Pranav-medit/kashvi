import json
import os
# import main


theme = {
    'black_theme': {
        'app-bg': '#404040',
        'app-disp-bg': '#d1e7dd',
        'n1-txt': 'white',
        'h1-txt': '#0b3b24',
        'h2-txt': '#0b3b24',
        'main-txt': '#0f5132',
        'btn': {
            'start-bg': '#0275d8',
            'start-fg': 'white',
            'stop-bg': '#ff0000',
            'stop-fg': 'white',
            'rstart-bg': 'green',
            'rstart-fg': 'white',
        }
    },
    'white_theme': {
        'app-bg': 'white',
        'app-disp-bg': '#ffe7c9',
        'n1-txt': '#404040',
        'h1-txt': '#cc7100',
        'h2-txt': '#cc7100',
        'main-txt': '#e07c00',
        'btn': {
            'start-bg': '#0275d8',
            'start-fg': 'white',
            'stop-bg': '#ff0000',
            'stop-fg': 'white',
            'rstart-bg': 'green',
            'rstart-fg': 'white',
        }
    },
    'orange_theme': {
        'app-bg': '#ff7700',
        'app-disp-bg': '#ffd2ab',
        'n1-txt': 'white',
        'h1-txt': '#de5c00',
        'h2-txt': '#de5c00',
        'main-txt': '#ff6a00',
        'btn': {
            'start-bg': '#0275d8',
            'start-fg': 'white',
            'stop-bg': '#ff0000',
            'stop-fg': 'white',
            'rstart-bg': 'green',
            'rstart-fg': 'white',
        }
    },
    'blue_theme': {
        'app-bg': '#00ffee',
        'app-disp-bg': '#00a196',
        'n1-txt': '#404040',
        'h1-txt': '#960000',
        'h2-txt': '#960000',
        'main-txt': '#b50000',
        'btn': {
            'start-bg': '#0275d8',
            'start-fg': 'white',
            'stop-bg': '#ff0000',
            'stop-fg': 'white',
            'rstart-bg': 'green',
            'rstart-fg': 'white',
        }
    }
}


commands = {
    'time': ['ಟೈಮ್', 'ಟೈಮ್ ಎಷ್ಟು', 'ಗಂಟೆ ಎಷ್ಟು', 'ಟೈಮೆಷ್ಟು', 'ಸಮಯ ಎಷ್ಟು', 'ಸಮಯವೆಷ್ಟು'],
    'news': ['ವಾರ್ತೆ ತಿಳಿಸು', 'ನ್ಯೂಸ್ ತಿಳಿಸು', 'ಮುಖ್ಯ ವಾರ್ತೆ ತಿಳಿಸು', 'ಸುದ್ದಿ ತಿಳಿಸು'],
    'wikipedia': ['ವಿಕಿಪಿಡಿಯಾ','ವಿಕಿಪೇಡಿಯ','ವಿಕಿಪೀಡಿಯಾ', 'ವಿಕಿಪೀಡಿಯ'],
    'you-tube': ['ಯೂಟ್ಯೂಬ್ ಅನ್ನು ತೆರೆಯಿರಿ', 'ಯೂಟ್ಯೂಬ್ ತೆರೆ', 'ಯುಟ್ಯೂಬ ಓಪನ್', 'ಓಪನ್ ಯುಟ್ಯೂಬ', 'ಓಪನ್ ಯುಟ್ಯೂಬ್',
                 'ಯುಟ್ಯೂಬ್ ','ಯೂಟ್ಯೂಬ್'],
    'google': ['ಗೂಗಲ್ ಅನ್ನು ತೆರೆಯಿರಿ', 'ಗೂಗಲ್ ತೆರೆ', 'ಗೂಗಲ್ ಓಪನ್', 'ಓಪನ್ ಗೂಗಲ್'],
    'weather': ['ವೆದರ್', 'ಹವಾಮಾನ', 'ವಾತಾವರಣ'],
    'whatsapp': ['ವಾಟ್ಸಪ್', 'ವಾಟ್ಸಾಪ್'],
    'restart': ['ರೀಸ್ಟಾರ್ಟ್ ಕಂಪ್ಯೂಟರ್','ಕಂಪ್ಯೂಟರ್ ರೀಸ್ಟಾರ್ಟ್', 'ಗಣಕಯಂತ್ರವನ್ನು ಮರು ಪ್ರಾರಂಭಿಸು',
                'ಗಣಕಯಂತ್ರವನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ'],
    'sleep': ['ಗಣಕಯಂತ್ರವನ್ನು ಮಲಗಿಸು', 'ಗಣಕಯಂತ್ರ ಮಲಗು','ಕಂಪ್ಯೂಟರ್ ಮಲಗು','ಕಂಪ್ಯೂಟರ್ ಮಲಗಿಸು',
                'ಸ್ಲೀಪ್ ಕಂಪ್ಯೂಟರ್', 'ಕಂಪ್ಯೂಟರ್ ಸ್ಲೀಪ್', 'ಮುಚ್ಕೋ ಮಲ್ಕ','ಮುಚ್ಕೊಂಡ್ ಮಲ್ಕೋ', 'ಮುಚ್ಕೊಂಡು ಮಲ್ಕ'],
    'power-off': ['ಕಂಪ್ಯೂಟರ್ ಕೆಡಿಸು', 'ಕಂಪ್ಯೂಟರ್ ಆರಿಸು', 'ಗಣಕಯಂತ್ರವನ್ನು ಆರಿಸು', 'ಗಣಕಯಂತ್ರವನ್ನು ಕೆಡಿಸು',
                  'ಶಟ್ ಡೌನ್ ಕಂಪ್ಯೂಟರ್', 'ಕಂಪ್ಯೂಟರ್ ಶಬ್ದೊನ್', 'ಕಂಪ್ಯೂಟರನ್ನು ಆರಿಸು'],
    'google-text': ['ಗೂಗಲ್', 'ಗೋಗಲ್', 'ಗಾಗಲ್'],
    'map': ['ಮ್ಯಾಪ್','ಮ್ಯಾಪ್ಸ್','ನಕ್ಷೆ'],
    'twitter':['ಟ್ವಿಟರ್ ತೆರೆ','ಟ್ವಿಟರ್ ಓಪನ್','ಓಪನ್ ಟ್ವಿಟರ್'],
    'facebook':['ಓಪನ್ ಫೇಸ್ಬುಕ್','ಫೇಸ್ಬುಕ್ ಓಪನ್','ಫೇಸ್ಬುಕ್ ತೆರೆ','ತೆರೆ ಫೇಸ್ಬುಕ್'],
    'instagram':['ಇನ್ಸ್ಟಾಗ್ರಾಮ್ ಓಪನ್','ಓಪನ್ ಇನ್ಸ್ಟಾಗ್ರಾಮ್','ತೆರೆ ಇನ್ಸ್ಟಾಗ್ರಾಮ್','ಇನ್ಸ್ಟಾಗ್ರಾಮ್ ತೆರೆ','ಓಪನ್ ಇನ್ಸ್ಟಾ'
        ,'ಇನ್ಸ್ಟಾ ಓಪನ್'],
    'e-mail':['ಇ-ಮೇಲ್ ಕಳಿಸು','ಇ-ಮೇಲ್','ಇಮೇಲ್ ಕಳುಹಿಸು'],
    'positive-statements': ['ಹೌದು', 'ಹಾ', 'ಎಸ್', 'ಓಕೆ'],
    'negative-statements': ['ನೋ', 'ಇಲ್ಲ', 'ಅಲ್ಲ'],
    'meaning':['ಶಬ್ದದ ಅರ್ಥ','ಶಬ್ದ ಅರ್ಥ','ಶಬ್ದಾರ್ಥ','ಮೀನಿಂಗ್','ಬಗ್ಗೆ','ಬಗ್ಗೆ ತಿಳಿಸು','ತಿಳಿಸು'],
}


# Error code settings
error_codes  = {
    'internet-error': {
        'etks':1000,
        'newsteller':1001,
        'weather-report':1003,
        'browser-open':1004,
        'google-search':1005,
        'youtube-link':1006,
        'mail':1007
    },
    'unknown-error': {
        'newsteller':1008,
        'notification':1009,
        'weather-report':1010,
        'google-maps':1011,
    },
    'dir-error':{
        'dir':1012,
    },
    'whatsapp':{
        'msg-error':1013,
    },
    'power':{
        'tweak-power':1014,
    }
}


# Array of bad words
def handle_d_error(callback_func):
    def decorator_function(*args, **kwargs):
        result = ''
        try:
            result = callback_func(*args)
        except FileNotFoundError as e:
            print("File not found error")
            main.error_message(f"Error occurred inside e[{callback_func.__name__}]",
                          'Error Details: \n' + 'File Not Found'+str(e).capitalize(), 3)
        except OSError as e:
            main.error_message(f"Error occurred inside e[{callback_func.__name__}]",
                               'Error Details: \n' + 'OS Error occurred' + str(e).capitalize(), 3)
        except Exception as e:
            print(f"Error occurred inside [" + callback_func.__name__ + "]")
            main.error_message(f"Error occurred inside e[{callback_func.__name__}]",'Error Details: \n'+str(e).capitalize(), 3)
        return result
    return decorator_function


# This function takes in a json file and array and converts that array into json file inside data directory
# EX: write_jsonfile('commands.json',commands)
@handle_d_error
def write_jsonfile(filename,filedata,dir='data'):
    filepath = os.path.join(dir,filename)
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(filepath, 'w') as fp:
        json.dump(filedata, fp, indent=1)
""

# Reading json file, This returns an array contained in json file
# EX: read_jsonfile('commands.json')
@handle_d_error
def read_jsonfile(filename,dir='data'):
    filepath = os.path.join(dir,filename)
    with open(filepath,'r') as fp:
        res = json.load(fp)
    return res


# Takes filenames and filedatas in list format and rewrites it note that length of both parameters should be equal
@handle_d_error
def update_json_files(filenames, filedatas):
    if type(filenames) is list and type(filedatas) is list and len(filenames) == len(filedatas):
        list(map(lambda i_item,j_item: write_jsonfile(i_item,j_item), filenames,filedatas))
    else:
        print("Error occurred,make sure that you have passed list only and length of list is same")


# This adds indentation
@handle_d_error
def jp(json_data,indent=1):
    return json.dumps(json_data, indent=indent, ensure_ascii=False)


# Given an array/list of filenames it returns parsed json and prettified(indented) json
@handle_d_error
def retrieve_json_files(filenames):
    prettified_json = []
    parsed_json = []
    for fn in filenames:
        res = read_jsonfile(fn)
        parsed_json.append(json.loads(jp(res,1)))
        prettified_json.append(jp(res,1))
    return [parsed_json,prettified_json]


# Prints json
@handle_d_error
def print_json(json_list,func=print):
    with open('file','r') as e:
        print(e.read())
    for json in json_list:
        func(json)


if __name__ == '__main__':
    # update_json_files(['kan_joke.json'],[jokes_arr])
    write_jsonfile('commands.json',commands)
    # update_json_files(['filenames1','filenames2'], ['filedatas1','filenamesdata2'])
    # for _ in range(4):
    #     import pyjokes
    #     str = pyjokes.get_joke()
    #     print(main.text_translator(str))
    #     print(str)
    #     from joke import generate

        # generate()
    # print_json(retrieve_json_files(['commands.json'])[1])
    pass

# Update json files
# for i_index,i_item in enumerate(filenames):
#     for j_index,j_item in enumerate(filedatas):
#         if i_index == j_index:
#             write_jsonfile(i_item,j_item)

