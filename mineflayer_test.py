import requests
import json
def begin():
    reset_options = {
            "port": 37275,#input the tcp port
            "reset": "soft",
            "inventory": {},
            "equipment": [],
            "spread": False,
            "waitTicks": 5,
            "position": None,
            }
    request_timeout = 600
    res = requests.post(
                    "http://127.0.0.1:3000/start",
                    json=reset_options,
                    timeout=request_timeout
                )

def act_test(code):
    request_timeout = 600
    with open('programs.txt','r') as file:
        programs = file.read()
        data = {
        "code": code,
        "programs": programs,
        }
        res = requests.post(
                "http://127.0.0.1:3000/step",
                json=data,
                timeout=request_timeout
                )
        events = res.json()
        events = json.loads(events)
        status_printer(events)

def status_printer(events):
    print('inventory:')
    print(events[-1][1]["inventory"])
    print('voxels:')
    print(events[-1][1]["voxels"])
    print('entities:')
    print(events[-1][1]["status"]['entities'])
    print('health:')
    print(events[-1][1]["status"]['health'])
    print('hunger:')
    print(events[-1][1]["status"]['food'])
    print('position:')
    print(events[-1][1]["status"]['position'])
    print('equipment:')
    print(events[-1][1]["status"]['equipment'])

def code_generator():
    code1 = input('please input your act:')
    code2 = input('input arg1:')
    code3  = input('input arg2:')
    if(code1 == 'v'):
        code = ''
    if(code1 == 'm'):
        code = f"mineBlock(bot,'{code2}',{code3})"
    if(code1 == 'c'):
        code = f"craftItem(bot,'{code2}',{code3})"
    if(code1 == 's'):
        code = f"smeltItem(bot,'{code2}',{code3})"
    if(code1 == 'p'):
        code = f"placeItem(bot,'{code2}',{code3})"
    if(code1 == 'k'):
        code = f"killMob(bot,'{code2}',{code3})"
    if(code1 == 'e'):
        code = f"exploreUntil(bot,new Vec3({code2}),{code3},() => {{}})"
        
    if(code1 == 'N'): #go to the nether
    	code = f"createNetherDoor(bot)"
    if(code1 == 'fw'):#fetch the water
    	code = f"fetchWater(bot)"
    if(code1 == 'fl'):#fetch the lava
    	code = f"fetchLava(bot)"
    if(code1 == 'cc'):#make a container to mix water and lava
    	code = f"createContainer(bot)"
    if(code1 == 'o'):#cool down the lava and get the obsidian
    	code = f"createObsidian(bot)"	
    if(code1 == 'gN'):#go to Nether
    	code = f"goToNether(bot)"	
    if(code1 == 'cB'):#combat blaze
    	code = f"combatBlaze(bot)"	
    	
        #print(code1)
    return code

begin()
while True:
    code = code_generator()
    act_test(code)
