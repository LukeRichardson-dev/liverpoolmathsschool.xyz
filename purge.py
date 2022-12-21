from codecs import utf_8_decode
import os

STATIC_EXTENSIONS = ['.jpg', '.svg', '.png', '.pdf']


def purge(path):
    print(path)
    for a, _, c in os.walk(path):
        for i in c:
            p = a + '\\' + i
            if any(map(lambda x: x.lower() in i, STATIC_EXTENSIONS)):
                continue
            try:
                
                with open(p, 'rb') as f:
                    cont, _ = utf_8_decode(f.read())

                if 'DOCTYPE' in cont:
                    cont = cont.replace('https://liverpoolmathsschool.org', 'http://localhost')
                    print(cont)
                    with open(p, 'wb') as f:
                        f.write(cont.encode())

            except Exception as e:
                print('failed', p, e)

if __name__ == '__main__':

    purge('C:\\Users\\richa\\Development\\remote\\liverpoolmathsschool.xyz\\site_test')