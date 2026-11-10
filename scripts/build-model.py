"""Original procedural investigative GPU sculpture. glTF 2.0 for Helios, no third-party assets."""
import json, struct, math, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
materials=[]
def mat(name,color,metal=0,rough=.5,emission=None):
    m={'name':name,'pbrMetallicRoughness':{'baseColorFactor':[*color,1],'metallicFactor':metal,'roughnessFactor':rough}}
    if emission:m['emissiveFactor']=emission
    materials.append(m);return len(materials)-1
pcb=mat('Graphite circuit substrate',[.022,.045,.025],.3,.6)
black=mat('Memory packages',[.025,.03,.028],.45,.32)
metal=mat('Brushed metal',[.24,.29,.26],.85,.3)
gold=mat('Gold contacts',[.39,.29,.08],.75,.32)
lime=mat('Signal traces',[.21,.46,.015],.4,.35,[.12,.36,.008])
die=mat('Silicon die',[.10,.18,.075],.9,.2)
floor=mat('Investigation desk',[.012,.017,.014],.15,.6)
groups={}
def box(c,s,m):
    p,n,idx=groups.setdefault(m,([],[],[])); x,y,z=c; a,b,d=[v/2 for v in s]
    faces=[([(x-a,y-b,z+d),(x+a,y-b,z+d),(x+a,y+b,z+d),(x-a,y+b,z+d)],(0,0,1)), ([(x+a,y-b,z-d),(x-a,y-b,z-d),(x-a,y+b,z-d),(x+a,y+b,z-d)],(0,0,-1)), ([(x+a,y-b,z+d),(x+a,y-b,z-d),(x+a,y+b,z-d),(x+a,y+b,z+d)],(1,0,0)), ([(x-a,y-b,z-d),(x-a,y-b,z+d),(x-a,y+b,z+d),(x-a,y+b,z-d)],(-1,0,0)), ([(x-a,y+b,z+d),(x+a,y+b,z+d),(x+a,y+b,z-d),(x-a,y+b,z-d)],(0,1,0)), ([(x-a,y-b,z-d),(x+a,y-b,z-d),(x+a,y-b,z+d),(x-a,y-b,z+d)],(0,-1,0))]
    for vs,no in faces:
        i=len(p)//3
        for v in vs:p.extend(v);n.extend(no)
        idx.extend([i,i+1,i+2,i,i+2,i+3])
# Exploded processor sculpture, horizontal board with actual depth, contacts and silicon.
box((0,.1,0),(14,.2,14),floor)
box((0,.44,0),(4.4,.18,4.4),black)
box((0,.64,0),(4.65,.12,4.65),pcb)
box((0,.88,0),(2.65,.22,2.65),metal)
box((0,1.05,0),(2.43,.14,2.43),black)
box((0,1.15,0),(1.8,.08,1.8),die)
for x in range(8):
    for z in range(8):
        box((-.77+x*.22,1.196,-.77+z*.22),(.185,.012,.185),lime if (x+z)%4==0 else die)
for side in [-1,1]:
    for i in range(5):
        v=-1.6+i*.8
        box((side*1.83,.82,v),(.48,.23,.52),black)
        box((v,.82,side*1.83),(.52,.23,.48),black)
    for i in range(28):
        v=-2.12+i*.157
        box((v,.59,side*2.4),(.065,.09,.23),gold)
        box((side*2.4,.59,v),(.23,.09,.065),gold)
    for i in range(19):
        v=-2.13+i*.23
        length=.24+(i%4)*.07
        box((v,.708,side*(2.12-length/2)),(.015,.012,length),lime)
        box((side*(2.12-length/2),.708,v),(length,.012,.015),lime)
    for i in range(11):
        v=-1.5+i*.3
        box((v,.714,side*1.48),(.06,.06,.12),metal)
        box((side*1.48,.714,v),(.12,.06,.06),metal)
for side in [-1,1]:
    box((side*2.26,.71,0),(.018,.02,4.45),lime)
    box((0,.71,side*2.26),(4.45,.02,.018),lime)
# Floor tracks provide a spatial visual metaphor; they do not encode factual data.
for i in range(-5,6):
    box((i*1.2,.206,0),(.008,.004,13),metal)
    box((0,.206,i*1.2),(13,.004,.008),metal)
buf=bytearray(); views=[]; access=[]; primitives=[]
def add(values,fmt,typ,component):
    while len(buf)%4:buf.append(0)
    start=len(buf);buf.extend(struct.pack('<'+fmt*len(values),*values)); vi=len(views)
    views.append({'buffer':0,'byteOffset':start,'byteLength':len(buf)-start})
    count=len(values)//(3 if typ=='VEC3' else 1)
    a={'bufferView':vi,'componentType':component,'count':count,'type':typ}
    if typ=='VEC3':a.update(min=[min(values[j::3]) for j in range(3)],max=[max(values[j::3]) for j in range(3)])
    access.append(a);return len(access)-1
for m,(p,n,idx) in groups.items():
    primitives.append({'attributes':{'POSITION':add(p,'f','VEC3',5126),'NORMAL':add(n,'f','VEC3',5126)},'indices':add(idx,'I','SCALAR',5125),'material':m})
doc={'asset':{'version':'2.0','generator':'Huang-akta procedural model / Helios'},'scene':0,'scenes':[{'nodes':[0]}],'nodes':[{'mesh':0}],'meshes':[{'name':'Evidence processor','primitives':primitives}],'materials':materials,'buffers':[{'byteLength':len(buf)}],'bufferViews':views,'accessors':access}
j=json.dumps(doc,separators=(',',':')).encode();j+=b' '*((-len(j))%4);buf+=b'\0'*((-len(buf))%4)
out=struct.pack('<III',0x46546c67,2,12+8+len(j)+8+len(buf))+struct.pack('<II',len(j),0x4e4f534a)+j+struct.pack('<II',len(buf),0x004e4942)+buf
(root/'public/models/evidence-chip.glb').write_bytes(out)
scene={'format':'helios-scene','version':1,'base':{'kind':'gltf','url':'./models/evidence-chip.glb','ground':False},'render':{'clouds':False,'volumetric_fog':False,'aerial_perspective':False,'wind':False,'motion_blur':0,'bloom_intensity':.045,'exposure_compensation':0,'auto_exposure':False,'local_exposure':False},'environment':{'sun_azimuth_deg':220,'sun_elevation_deg':48,'sun_intensity':5,'fog':{'density':0,'height_falloff':.2,'base_height':0,'albedo':[.5,.5,.5],'anisotropy':0,'ambient':0,'noise':0,'distance':100},'clouds':{'coverage':0,'density':0,'base_altitude':1000,'thickness':100,'wind':[0,0],'shadow_strength':0},'wind':{'direction':[1,0],'strength':0,'gust_frequency':0,'gust_wavelength':1,'turbulence':0}}}
(root/'public/chip.helios.json').write_text(json.dumps(scene),encoding='utf8')
print(f'Wrote {len(out):,} byte glb with {sum(len(v[2])//3 for v in groups.values()):,} triangles')

