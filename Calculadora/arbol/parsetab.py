
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONDIVISIONINT FLOAT NAME RESTA SUMA DIVISION MULTIPLICACION EQUALS\n    calc : expression\n         | var_assign\n         | empty\n    \n    var_assign : NAME EQUALS expression\n        \n    \n    expression : expression MULTIPLICACION expression\n               | expression DIVISION expression\n               | expression SUMA expression\n               | expression RESTA expression\n    \n    expression : INT\n               | FLOAT\n    \n    expression : NAME\n    \n    empty : \n    '
    
_lr_action_items = {'INT':([0,8,9,10,11,12,],[5,5,5,5,5,5,]),'FLOAT':([0,8,9,10,11,12,],[6,6,6,6,6,6,]),'NAME':([0,8,9,10,11,12,],[7,14,14,14,14,14,]),'$end':([0,1,2,3,4,5,6,7,13,14,15,16,17,18,],[-12,0,-1,-2,-3,-9,-10,-11,-5,-11,-6,-7,-8,-4,]),'MULTIPLICACION':([2,5,6,7,13,14,15,16,17,18,],[8,-9,-10,-11,-5,-11,-6,8,8,8,]),'DIVISION':([2,5,6,7,13,14,15,16,17,18,],[9,-9,-10,-11,-5,-11,-6,9,9,9,]),'SUMA':([2,5,6,7,13,14,15,16,17,18,],[10,-9,-10,-11,-5,-11,-6,-7,-8,10,]),'RESTA':([2,5,6,7,13,14,15,16,17,18,],[11,-9,-10,-11,-5,-11,-6,-7,-8,11,]),'EQUALS':([7,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,8,9,10,11,12,],[2,13,15,16,17,18,]),'var_assign':([0,],[3,]),'empty':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','calc.py',61),
  ('calc -> var_assign','calc',1,'p_calc','calc.py',62),
  ('calc -> empty','calc',1,'p_calc','calc.py',63),
  ('var_assign -> NAME EQUALS expression','var_assign',3,'p_var_assign','calc.py',70),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression','calc.py',78),
  ('expression -> expression DIVISION expression','expression',3,'p_expression','calc.py',79),
  ('expression -> expression SUMA expression','expression',3,'p_expression','calc.py',80),
  ('expression -> expression RESTA expression','expression',3,'p_expression','calc.py',81),
  ('expression -> INT','expression',1,'p_expression_int_float','calc.py',90),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','calc.py',91),
  ('expression -> NAME','expression',1,'p_expression_var','calc.py',97),
  ('empty -> <empty>','empty',0,'p_empty','calc.py',106),
]
