from contracts.contract_library import *
from goal_model import *
from ttictoc import TicToc

t = TicToc()

contract_library = ContractLibrary("cogomo")

p0 = Bool('p0')
p1 = Bool('p1')
p2 = Bool('p2')
p3 = Bool('p3')
p4 = Bool('p4')
p5 = Bool('p5')
p6 = Bool('p6')
p7 = Bool('p7')
p8 = Bool('p8')
p9 = Bool('p9')
p10 = Bool('p10')
p11 = Bool('p11')
p12 = Bool('p12')
p13 = Bool('p13')
p14 = Bool('p14')
p15 = Bool('p15')
p16 = Bool('p16')
p17 = Bool('p17')
p18 = Bool('p18')
p19 = Bool('p19')
p20 = Bool('p20')
p21 = Bool('p21')
p22 = Bool('p22')
p23 = Bool('p23')
p24 = Bool('p24')
p25 = Bool('p25')
p26 = Bool('p26')
p27 = Bool('p27')
p28 = Bool('p28')
p29 = Bool('p29')
p30 = Bool('p30')
p31 = Bool('p31')
p32 = Bool('p32')
p33 = Bool('p33')
p34 = Bool('p34')
p35 = Bool('p35')
p36 = Bool('p36')
p37 = Bool('p37')
p38 = Bool('p38')
p39 = Bool('p39')
p40 = Bool('p40')
p41 = Bool('p41')
p42 = Bool('p42')
p43 = Bool('p43')
p44 = Bool('p44')
p45 = Bool('p45')
p46 = Bool('p46')
p47 = Bool('p47')
p48 = Bool('p48')
p49 = Bool('p49')
p50 = Bool('p50')
p51 = Bool('p51')
p52 = Bool('p52')
p53 = Bool('p53')
p54 = Bool('p54')
p55 = Bool('p55')
p56 = Bool('p56')
p57 = Bool('p57')
p58 = Bool('p58')
p59 = Bool('p59')
p60 = Bool('p60')
p61 = Bool('p61')
p62 = Bool('p62')
p63 = Bool('p63')
p64 = Bool('p64')
p65 = Bool('p65')
p66 = Bool('p66')
p67 = Bool('p67')
p68 = Bool('p68')
p69 = Bool('p69')
p70 = Bool('p70')
p71 = Bool('p71')
p72 = Bool('p72')
p73 = Bool('p73')
p74 = Bool('p74')
p75 = Bool('p75')
p76 = Bool('p76')
p77 = Bool('p77')
p78 = Bool('p78')
p79 = Bool('p79')
p80 = Bool('p80')
p81 = Bool('p81')
p82 = Bool('p82')
p83 = Bool('p83')
p84 = Bool('p84')
p85 = Bool('p85')
p86 = Bool('p86')
p87 = Bool('p87')
p88 = Bool('p88')
p89 = Bool('p89')
p90 = Bool('p90')
p91 = Bool('p91')
p92 = Bool('p92')
p93 = Bool('p93')
p94 = Bool('p94')
p95 = Bool('p95')
p96 = Bool('p96')
p97 = Bool('p97')
p98 = Bool('p98')
p99 = Bool('p99')
p100 = Bool('p100')
p101 = Bool('p101')
p102 = Bool('p102')
p103 = Bool('p103')
p104 = Bool('p104')
p105 = Bool('p105')
p106 = Bool('p106')
p107 = Bool('p107')
p108 = Bool('p108')
p109 = Bool('p109')
p110 = Bool('p110')
p111 = Bool('p111')
p112 = Bool('p112')
p113 = Bool('p113')
p114 = Bool('p114')
p115 = Bool('p115')
p116 = Bool('p116')
p117 = Bool('p117')
p118 = Bool('p118')
p119 = Bool('p119')
p120 = Bool('p120')
p121 = Bool('p121')
p122 = Bool('p122')
p123 = Bool('p123')
p124 = Bool('p124')
p125 = Bool('p125')
p126 = Bool('p126')
p127 = Bool('p127')
p128 = Bool('p128')
p129 = Bool('p129')
p130 = Bool('p130')
p131 = Bool('p131')
p132 = Bool('p132')
p133 = Bool('p133')
p134 = Bool('p134')
p135 = Bool('p135')
p136 = Bool('p136')
p137 = Bool('p137')
p138 = Bool('p138')
p139 = Bool('p139')
p140 = Bool('p140')
p141 = Bool('p141')
p142 = Bool('p142')
p143 = Bool('p143')
p144 = Bool('p144')
p145 = Bool('p145')
p146 = Bool('p146')
p147 = Bool('p147')
p148 = Bool('p148')
p149 = Bool('p149')
p150 = Bool('p150')
p151 = Bool('p151')
p152 = Bool('p152')
p153 = Bool('p153')
p154 = Bool('p154')
p155 = Bool('p155')
p156 = Bool('p156')
p157 = Bool('p157')
p158 = Bool('p158')
p159 = Bool('p159')
p160 = Bool('p160')
p161 = Bool('p161')
p162 = Bool('p162')
p163 = Bool('p163')
p164 = Bool('p164')
p165 = Bool('p165')
p166 = Bool('p166')
p167 = Bool('p167')
p168 = Bool('p168')
p169 = Bool('p169')
p170 = Bool('p170')
p171 = Bool('p171')
p172 = Bool('p172')
p173 = Bool('p173')
p174 = Bool('p174')
p175 = Bool('p175')
p176 = Bool('p176')
p177 = Bool('p177')
p178 = Bool('p178')
p179 = Bool('p179')
p180 = Bool('p180')
p181 = Bool('p181')
p182 = Bool('p182')
p183 = Bool('p183')
p184 = Bool('p184')
p185 = Bool('p185')
p186 = Bool('p186')
p187 = Bool('p187')
p188 = Bool('p188')
p189 = Bool('p189')
p190 = Bool('p190')
p191 = Bool('p191')
p192 = Bool('p192')
p193 = Bool('p193')
p194 = Bool('p194')
p195 = Bool('p195')
p196 = Bool('p196')
p197 = Bool('p197')
p198 = Bool('p198')
p199 = Bool('p199')
p200 = Bool('p200')
p201 = Bool('p201')
p202 = Bool('p202')
p203 = Bool('p203')
p204 = Bool('p204')
p205 = Bool('p205')
p206 = Bool('p206')
p207 = Bool('p207')
p208 = Bool('p208')
p209 = Bool('p209')
p210 = Bool('p210')
p211 = Bool('p211')
p212 = Bool('p212')
p213 = Bool('p213')
p214 = Bool('p214')
p215 = Bool('p215')
p216 = Bool('p216')
p217 = Bool('p217')
p218 = Bool('p218')
p219 = Bool('p219')
p220 = Bool('p220')
p221 = Bool('p221')
p222 = Bool('p222')
p223 = Bool('p223')
p224 = Bool('p224')
p225 = Bool('p225')
p226 = Bool('p226')
p227 = Bool('p227')
p228 = Bool('p228')
p229 = Bool('p229')
p230 = Bool('p230')
p231 = Bool('p231')
p232 = Bool('p232')
p233 = Bool('p233')
p234 = Bool('p234')
p235 = Bool('p235')
p236 = Bool('p236')
p237 = Bool('p237')
p238 = Bool('p238')
p239 = Bool('p239')
p240 = Bool('p240')
p241 = Bool('p241')
p242 = Bool('p242')
p243 = Bool('p243')
p244 = Bool('p244')
p245 = Bool('p245')
p246 = Bool('p246')
p247 = Bool('p247')
p248 = Bool('p248')
p249 = Bool('p249')
p250 = Bool('p250')
p251 = Bool('p251')
p252 = Bool('p252')
p253 = Bool('p253')
p254 = Bool('p254')
p255 = Bool('p255')
p256 = Bool('p256')
p257 = Bool('p257')
p258 = Bool('p258')
p259 = Bool('p259')
p260 = Bool('p260')
p261 = Bool('p261')
p262 = Bool('p262')
p263 = Bool('p263')
p264 = Bool('p264')
p265 = Bool('p265')
p266 = Bool('p266')
p267 = Bool('p267')
p268 = Bool('p268')
p269 = Bool('p269')
p270 = Bool('p270')
p271 = Bool('p271')
p272 = Bool('p272')
p273 = Bool('p273')
p274 = Bool('p274')
p275 = Bool('p275')
p276 = Bool('p276')
p277 = Bool('p277')
p278 = Bool('p278')
p279 = Bool('p279')
p280 = Bool('p280')
p281 = Bool('p281')
p282 = Bool('p282')
p283 = Bool('p283')
p284 = Bool('p284')
p285 = Bool('p285')
p286 = Bool('p286')
p287 = Bool('p287')
p288 = Bool('p288')
p289 = Bool('p289')
p290 = Bool('p290')
p291 = Bool('p291')
p292 = Bool('p292')
p293 = Bool('p293')
p294 = Bool('p294')
p295 = Bool('p295')
p296 = Bool('p296')
p297 = Bool('p297')
p298 = Bool('p298')
p299 = Bool('p299')
p300 = Bool('p300')
p301 = Bool('p301')
p302 = Bool('p302')
p303 = Bool('p303')
p304 = Bool('p304')
p305 = Bool('p305')
p306 = Bool('p306')
p307 = Bool('p307')
p308 = Bool('p308')
p309 = Bool('p309')
p310 = Bool('p310')
p311 = Bool('p311')
p312 = Bool('p312')
p313 = Bool('p313')
p314 = Bool('p314')
p315 = Bool('p315')
p316 = Bool('p316')
p317 = Bool('p317')
p318 = Bool('p318')
p319 = Bool('p319')
p320 = Bool('p320')
p321 = Bool('p321')
p322 = Bool('p322')
p323 = Bool('p323')
p324 = Bool('p324')
p325 = Bool('p325')
p326 = Bool('p326')
p327 = Bool('p327')
p328 = Bool('p328')
p329 = Bool('p329')
p330 = Bool('p330')
p331 = Bool('p331')
p332 = Bool('p332')
p333 = Bool('p333')
p334 = Bool('p334')
p335 = Bool('p335')
p336 = Bool('p336')
p337 = Bool('p337')
p338 = Bool('p338')
p339 = Bool('p339')
p340 = Bool('p340')
p341 = Bool('p341')
p342 = Bool('p342')
p343 = Bool('p343')
p344 = Bool('p344')
p345 = Bool('p345')
p346 = Bool('p346')
p347 = Bool('p347')
p348 = Bool('p348')
p349 = Bool('p349')
p350 = Bool('p350')
p351 = Bool('p351')
p352 = Bool('p352')
p353 = Bool('p353')
p354 = Bool('p354')
p355 = Bool('p355')
p356 = Bool('p356')
p357 = Bool('p357')
p358 = Bool('p358')
p359 = Bool('p359')
p360 = Bool('p360')
p361 = Bool('p361')
p362 = Bool('p362')
p363 = Bool('p363')
p364 = Bool('p364')
p365 = Bool('p365')
p366 = Bool('p366')
p367 = Bool('p367')
p368 = Bool('p368')
p369 = Bool('p369')
p370 = Bool('p370')
p371 = Bool('p371')
p372 = Bool('p372')
p373 = Bool('p373')
p374 = Bool('p374')
p375 = Bool('p375')
p376 = Bool('p376')
p377 = Bool('p377')
p378 = Bool('p378')
p379 = Bool('p379')
p380 = Bool('p380')
p381 = Bool('p381')
p382 = Bool('p382')
p383 = Bool('p383')
p384 = Bool('p384')
p385 = Bool('p385')
p386 = Bool('p386')
p387 = Bool('p387')
p388 = Bool('p388')
p389 = Bool('p389')
p390 = Bool('p390')
p391 = Bool('p391')
p392 = Bool('p392')
p393 = Bool('p393')
p394 = Bool('p394')
p395 = Bool('p395')
p396 = Bool('p396')
p397 = Bool('p397')
p398 = Bool('p398')
p399 = Bool('p399')
p400 = Bool('p400')
p401 = Bool('p401')
p402 = Bool('p402')
p403 = Bool('p403')
p404 = Bool('p404')
p405 = Bool('p405')
p406 = Bool('p406')
p407 = Bool('p407')
p408 = Bool('p408')
p409 = Bool('p409')
p410 = Bool('p410')
p411 = Bool('p411')
p412 = Bool('p412')
p413 = Bool('p413')
p414 = Bool('p414')
p415 = Bool('p415')
p416 = Bool('p416')
p417 = Bool('p417')
p418 = Bool('p418')
p419 = Bool('p419')
p420 = Bool('p420')
p421 = Bool('p421')
p422 = Bool('p422')
p423 = Bool('p423')
p424 = Bool('p424')
p425 = Bool('p425')
p426 = Bool('p426')
p427 = Bool('p427')
p428 = Bool('p428')
p429 = Bool('p429')
p430 = Bool('p430')
p431 = Bool('p431')
p432 = Bool('p432')
p433 = Bool('p433')
p434 = Bool('p434')
p435 = Bool('p435')
p436 = Bool('p436')
p437 = Bool('p437')
p438 = Bool('p438')
p439 = Bool('p439')
p440 = Bool('p440')
p441 = Bool('p441')
p442 = Bool('p442')
p443 = Bool('p443')
p444 = Bool('p444')
p445 = Bool('p445')
p446 = Bool('p446')
p447 = Bool('p447')
p448 = Bool('p448')
p449 = Bool('p449')
p450 = Bool('p450')
p451 = Bool('p451')
p452 = Bool('p452')
p453 = Bool('p453')
p454 = Bool('p454')
p455 = Bool('p455')
p456 = Bool('p456')
p457 = Bool('p457')
p458 = Bool('p458')
p459 = Bool('p459')
p460 = Bool('p460')
p461 = Bool('p461')
p462 = Bool('p462')
p463 = Bool('p463')
p464 = Bool('p464')
p465 = Bool('p465')
p466 = Bool('p466')
p467 = Bool('p467')
p468 = Bool('p468')
p469 = Bool('p469')
p470 = Bool('p470')
p471 = Bool('p471')
p472 = Bool('p472')
p473 = Bool('p473')
p474 = Bool('p474')
p475 = Bool('p475')
p476 = Bool('p476')
p477 = Bool('p477')
p478 = Bool('p478')
p479 = Bool('p479')
p480 = Bool('p480')

contract_library.add_contracts(
    [
		Contract([p0 == True, p1 == True, p2 == True, p3 == True, p4 == True, p5 == True, p6 == True, p7 == True], [p8 == True, p9 == True, p10 == True, p11 == True, p12 == True, p13 == True, p14 == True, p15 == True], name="c0"),
		Contract([p15 == True, p16 == True, p17 == True, p18 == True, p19 == True, p20 == True, p21 == True, p22 == True], [p23 == True, p24 == True, p25 == True, p26 == True, p27 == True, p28 == True, p29 == True, p30 == True], name="c1"),
		Contract([p30 == True, p31 == True, p32 == True, p33 == True, p34 == True, p35 == True, p36 == True, p37 == True], [p38 == True, p39 == True, p40 == True, p41 == True, p42 == True, p43 == True, p44 == True, p45 == True], name="c2"),
		Contract([p45 == True, p46 == True, p47 == True, p48 == True, p49 == True, p50 == True, p51 == True, p52 == True], [p53 == True, p54 == True, p55 == True, p56 == True, p57 == True, p58 == True, p59 == True, p60 == True], name="c3"),
		Contract([p60 == True, p61 == True, p62 == True, p63 == True, p64 == True, p65 == True, p66 == True, p67 == True], [p68 == True, p69 == True, p70 == True, p71 == True, p72 == True, p73 == True, p74 == True, p75 == True], name="c4"),
		Contract([p75 == True, p76 == True, p77 == True, p78 == True, p79 == True, p80 == True, p81 == True, p82 == True], [p83 == True, p84 == True, p85 == True, p86 == True, p87 == True, p88 == True, p89 == True, p90 == True], name="c5"),
		Contract([p90 == True, p91 == True, p92 == True, p93 == True, p94 == True, p95 == True, p96 == True, p97 == True], [p98 == True, p99 == True, p100 == True, p101 == True, p102 == True, p103 == True, p104 == True, p105 == True], name="c6"),
		Contract([p105 == True, p106 == True, p107 == True, p108 == True, p109 == True, p110 == True, p111 == True, p112 == True], [p113 == True, p114 == True, p115 == True, p116 == True, p117 == True, p118 == True, p119 == True, p120 == True], name="c7"),
		Contract([p120 == True, p121 == True, p122 == True, p123 == True, p124 == True, p125 == True, p126 == True, p127 == True], [p128 == True, p129 == True, p130 == True, p131 == True, p132 == True, p133 == True, p134 == True, p135 == True], name="c8"),
		Contract([p135 == True, p136 == True, p137 == True, p138 == True, p139 == True, p140 == True, p141 == True, p142 == True], [p143 == True, p144 == True, p145 == True, p146 == True, p147 == True, p148 == True, p149 == True, p150 == True], name="c9"),
		Contract([p150 == True, p151 == True, p152 == True, p153 == True, p154 == True, p155 == True, p156 == True, p157 == True], [p158 == True, p159 == True, p160 == True, p161 == True, p162 == True, p163 == True, p164 == True, p165 == True], name="c10"),
		Contract([p165 == True, p166 == True, p167 == True, p168 == True, p169 == True, p170 == True, p171 == True, p172 == True], [p173 == True, p174 == True, p175 == True, p176 == True, p177 == True, p178 == True, p179 == True, p180 == True], name="c11"),
		Contract([p180 == True, p181 == True, p182 == True, p183 == True, p184 == True, p185 == True, p186 == True, p187 == True], [p188 == True, p189 == True, p190 == True, p191 == True, p192 == True, p193 == True, p194 == True, p195 == True], name="c12"),
		Contract([p195 == True, p196 == True, p197 == True, p198 == True, p199 == True, p200 == True, p201 == True, p202 == True], [p203 == True, p204 == True, p205 == True, p206 == True, p207 == True, p208 == True, p209 == True, p210 == True], name="c13"),
		Contract([p210 == True, p211 == True, p212 == True, p213 == True, p214 == True, p215 == True, p216 == True, p217 == True], [p218 == True, p219 == True, p220 == True, p221 == True, p222 == True, p223 == True, p224 == True, p225 == True], name="c14"),
		Contract([p225 == True, p226 == True, p227 == True, p228 == True, p229 == True, p230 == True, p231 == True, p232 == True], [p233 == True, p234 == True, p235 == True, p236 == True, p237 == True, p238 == True, p239 == True, p240 == True], name="c15"),
		Contract([p240 == True, p241 == True, p242 == True, p243 == True, p244 == True, p245 == True, p246 == True, p247 == True], [p248 == True, p249 == True, p250 == True, p251 == True, p252 == True, p253 == True, p254 == True, p255 == True], name="c16"),
		Contract([p255 == True, p256 == True, p257 == True, p258 == True, p259 == True, p260 == True, p261 == True, p262 == True], [p263 == True, p264 == True, p265 == True, p266 == True, p267 == True, p268 == True, p269 == True, p270 == True], name="c17"),
		Contract([p270 == True, p271 == True, p272 == True, p273 == True, p274 == True, p275 == True, p276 == True, p277 == True], [p278 == True, p279 == True, p280 == True, p281 == True, p282 == True, p283 == True, p284 == True, p285 == True], name="c18"),
		Contract([p285 == True, p286 == True, p287 == True, p288 == True, p289 == True, p290 == True, p291 == True, p292 == True], [p293 == True, p294 == True, p295 == True, p296 == True, p297 == True, p298 == True, p299 == True, p300 == True], name="c19"),
		Contract([p300 == True, p301 == True, p302 == True, p303 == True, p304 == True, p305 == True, p306 == True, p307 == True], [p308 == True, p309 == True, p310 == True, p311 == True, p312 == True, p313 == True, p314 == True, p315 == True], name="c20"),
		Contract([p315 == True, p316 == True, p317 == True, p318 == True, p319 == True, p320 == True, p321 == True, p322 == True], [p323 == True, p324 == True, p325 == True, p326 == True, p327 == True, p328 == True, p329 == True, p330 == True], name="c21"),
		Contract([p330 == True, p331 == True, p332 == True, p333 == True, p334 == True, p335 == True, p336 == True, p337 == True], [p338 == True, p339 == True, p340 == True, p341 == True, p342 == True, p343 == True, p344 == True, p345 == True], name="c22"),
		Contract([p345 == True, p346 == True, p347 == True, p348 == True, p349 == True, p350 == True, p351 == True, p352 == True], [p353 == True, p354 == True, p355 == True, p356 == True, p357 == True, p358 == True, p359 == True, p360 == True], name="c23"),
		Contract([p360 == True, p361 == True, p362 == True, p363 == True, p364 == True, p365 == True, p366 == True, p367 == True], [p368 == True, p369 == True, p370 == True, p371 == True, p372 == True, p373 == True, p374 == True, p375 == True], name="c24"),
		Contract([p375 == True, p376 == True, p377 == True, p378 == True, p379 == True, p380 == True, p381 == True, p382 == True], [p383 == True, p384 == True, p385 == True, p386 == True, p387 == True, p388 == True, p389 == True, p390 == True], name="c25"),
		Contract([p390 == True, p391 == True, p392 == True, p393 == True, p394 == True, p395 == True, p396 == True, p397 == True], [p398 == True, p399 == True, p400 == True, p401 == True, p402 == True, p403 == True, p404 == True, p405 == True], name="c26"),
		Contract([p405 == True, p406 == True, p407 == True, p408 == True, p409 == True, p410 == True, p411 == True, p412 == True], [p413 == True, p414 == True, p415 == True, p416 == True, p417 == True, p418 == True, p419 == True, p420 == True], name="c27"),
		Contract([p420 == True, p421 == True, p422 == True, p423 == True, p424 == True, p425 == True, p426 == True, p427 == True], [p428 == True, p429 == True, p430 == True, p431 == True, p432 == True, p433 == True, p434 == True, p435 == True], name="c28"),
		Contract([p435 == True, p436 == True, p437 == True, p438 == True, p439 == True, p440 == True, p441 == True, p442 == True], [p443 == True, p444 == True, p445 == True, p446 == True, p447 == True, p448 == True, p449 == True, p450 == True], name="c29"),
		Contract([p450 == True, p451 == True, p452 == True, p453 == True, p454 == True, p455 == True, p456 == True, p457 == True], [p458 == True, p459 == True, p460 == True, p461 == True, p462 == True, p463 == True, p464 == True, p465 == True], name="c30"),
		Contract([p465 == True, p466 == True, p467 == True, p468 == True, p469 == True, p470 == True, p471 == True, p472 == True], [p473 == True, p474 == True, p475 == True, p476 == True, p477 == True, p478 == True, p479 == True, p480 == True], name="c31")
	])

spec_a = []
spec_g = [p480 == True]

spec_contract = Contract(spec_a, spec_g, name="specification")


def run_16_32():
    t.tic()
    synthesize_goal(contract_library, spec_contract, "synthesised_goal")
    t.toc()
    return t.elapsed


if __name__ == '__main__':
    run_16_32()
