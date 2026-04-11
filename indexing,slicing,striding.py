Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="Gayathri Twisha"
>>> a[1]
'a'
>>> a[5]
'h'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]
'Gayathri'
>>> a=" I am in class"
>>> a[8]+a[9]+a[10]+a[11]
' cla'
>>> a[9]+a[10]+a[11]+a[12]+a[13]
'class'
>>> a[2]+a[3]+a[4]
' am'
>>> a='i am learning python'
>>> a[2]+a[3]
'am'
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> g='i am in work'
>>> a[2]+a[3]
'am'
>>> a[5]+a[6]
'le'
>>> g[2]+g[3]
'am'
>>> g[4]+g[5]
' i'
>>> g[5]+g[6]
'in'
>>> g[8]+g[9]+g[10]+g[11]
'work'
>>> a='simple is better than complex'
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
'xelpmoc'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
>>> a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-28]+a[-27]+a[-26]+a[-25]+a[-24]+a[-23]
'imple '
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
b='codegnan it solutions'
b[]
SyntaxError: invalid syntax
b[-9]+b[-8]+b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'solutions'
b[-21]+b[-20]+b[-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
'codegnan'
b[-12]+b[-11]
'it'
#slicing
a='codegnan'
a[0;3
  
SyntaxError: invalid syntax
a[0:3
  a[0:4]
  
SyntaxError: '[' was never closed
 a[0:3]
  
SyntaxError: unexpected indent
a[0:3]
  
'cod'
a[0:4]
  
'code'
a[:4]
  
'code'
a[4:]
  
'gnan'
a[4:8]
  
'gnan'
b='work hard until you succeed'
  
a[:4]
  
'code'
b[:4]
  
'work'
b[6:10]
  
'ard '
b[5:9]
  
'hard'
b[9:14]
  
' unti'
b[10:15]
  
'until'
b[16:19]
  
'you'
b[20:27]
  
'succeed'
c='Beautiful is better than ugly'
  
c[:10]
  
'Beautiful '
c[:9]
  
'Beautiful'
c[13:19]
  
'better'
c[25:29]
  
'ugly'
d='patience is strength'
  
d[-8:0]
  
''
d[-8:-1]
  
'strengt'
d[-8]
  
's'
d[-8:]
  
'strength'
d[-20:-12]
  
'patience'
e='sun rises in the east'
  
e[-4:]
  
'east'
e[-8:-5]
  
'the'
e[-17:-12]
  
'rises'
e[:-18]
  
'sun'
d[-8:-0]
  
''
d[-8:-]
  
SyntaxError: invalid syntax
#striding
  
a='cloud computing'
  
a[::5]
  
'c u'
a[::3]
  
'cucpi'
a[3:]
  
'ud computing'
a[:9]
  
'cloud com'
a[::7]
  
'cog'
a[5:11]
  
' compu'
a[::2]
  
'codcmuig'
b='machine learning'
  
b[2:14:3]
  
'cnlr'
b[3:15:5]
  
'hli'
b[3:13:4]
  
'h r'
b[2:12:6]
  
'cl'
a='python course'
  
a[-1:-9:-3]
  
'eu '
a[-4:-12:-4]
  
'un'
a[-3:-14:-2]
  
'ro otp'
