import PySimpleGUI as sg

tab1_layout = [
    [sg.T('Exposure Monitor') 
    ,sg.Button('Run Exposure Monitor')]
    ,[sg.T('Asset Monitor') 
    ,sg.Button('Run Asset Monitor')]
    ,[sg.T('Delinquency Monitor') 
    ,sg.Button('Run Delinquency Monitor')]
    ,[sg.T('Funding Monitor') 
    ,sg.Button('Run Funding Monitor')]
    ]

tab2_layout = [
    [sg.T('Run SQL Query')]
    ,[sg.InputText(), sg.FileBrowse()]
    ,[sg.T('Input Database')
    ,sg.Listbox(['prod', 'warehouse', 'gotrade'], no_scrollbar=False)
    ,sg.Button('Run SQL')]
    ]

tab3_layout = [
    [sg.T('test2')
    ,sg.FileBrowse()]
    ,[sg.Listbox([1,2,3,4,5], no_scrollbar=False)
    ,sg.InputText('input1', size=(4,1)) 
    ,sg.Button('test2')]
    ]

tab4_layout = [
    [sg.T('test3')]
    ,[sg.InputText('input3', size=(10,1))
    ,sg.Checkbox('check1') 
    ,sg.Checkbox('check2')
    ,sg.Checkbox('check3')]
    ,[sg.Button('test3')
    ,sg.Button('test3')]
    ]

layout = [
    [sg.Text('Capital Markets Tools'
        ,justification='center'
        ,size=(65,1))]
    ,[sg.TabGroup(
            [
            [sg.Tab('Portfolio Monitor', tab1_layout, tooltip='')
            ,sg.Tab('SQL Runner', tab2_layout, tooltip='', visible=True)
            ,sg.Tab('Forecasts (WIP)', tab3_layout, tooltip='', visible=True)
            ,sg.Tab('Analytics (WIP)', tab4_layout, tooltip='', visible=True)]
            ])]
    ,[sg.Quit()]
    ]

window = sg.Window('Capital Markets Tool Dashboard'
    ,layout
    ,element_padding=((4,4),(4,4))
    )


while True:
    event, values = window.Read()
    print(event, values)
    if event in ('Quit', None):
        break
    elif event == 'Run Exposure Monitor':
        from portfolio_monitor import exposure_monitor
    elif event == 'Run Asset Monitor':
        from portfolio_monitor import asset_monitor
    elif event == 'Run Delinquency Monitor':
        from portfolio_monitor import delinquency_monitor
    elif event == 'Run Funding Monitor':
        from portfolio_monitor import funding_monitor
    elif event == 'Run SQL':
        from db_connector import db
        sql = open(values['Browse'], 'r').read()
        df = db.get_data(sql, db=values[1][0])
        sg.PopupOK(df.head())
    elif event == 'test3':  
        print('foo3')
    elif event == 'foo4':
        print('bar4')
    elif event == 'foo5':
        print('bar5')