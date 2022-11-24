
% --- Outputs from this function are returned to the command line.
function varargout = LEDlagi2_OutputFcn(hObject, eventdata, handles) 
varargout{1} = handles.output;
clear all;
global a;
a = arduino;

% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
global a;
writeDigitalPin(a, 'D9',1);

% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
global a;
writeDigitalPin(a, 'D9',0);