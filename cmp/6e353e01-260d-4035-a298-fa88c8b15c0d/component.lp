(librepcb_component 6e353e01-260d-4035-a298-fa88c8b15c0d
 (name "Toggle Switch")
 (description "Single-Pole Double-Throw switch")
 (keywords "switch,spdt,single-pole,double-throw")
 (author "Antoine Gagniere")
 (version "0.1")
 (created 2024-06-08T23:45:57Z)
 (deprecated false)
 (generated_by "")
 (category e29f0cb3-ef6d-4203-b854-d75150cbae0b)
 (schematic_only false)
 (default_value "{{MPN or DEVICE}}")
 (prefix "S")
 (signal f3d03b91-f648-4411-a5c1-b5deb0a421dd (name "Up") (role passive)
  (required false) (negated false) (clock false) (forced_net "")
 )
 (signal 915b4448-2622-4dbf-9453-91d4dd4558ec (name "Down") (role passive)
  (required false) (negated false) (clock false) (forced_net "")
 )
 (signal f8e0bea4-c74e-4003-96de-ad2f43afaf13 (name "COM") (role passive)
  (required true) (negated false) (clock false) (forced_net "")
 )
 (variant 76b4395f-0162-4c0b-aab5-e9ee77af77d3 (norm "")
  (name "Default")
  (description "")
  (gate 7b1ca14e-fc0e-44ca-baa0-5523be6c315e
   (symbol 5545c308-f283-42d2-96b1-700f3453a468)
   (position 0.0 0.0) (rotation 0.0) (required true) (suffix "")
   (pin 137e9c8d-3743-4e3b-9180-1f54679e8808 (signal f3d03b91-f648-4411-a5c1-b5deb0a421dd) (text signal))
   (pin 9f6fbf8c-b41d-4d49-b68f-29d1779fbaaa (signal 915b4448-2622-4dbf-9453-91d4dd4558ec) (text signal))
   (pin bfee3d5d-9bdd-4dc8-88f2-34c0679963c0 (signal f8e0bea4-c74e-4003-96de-ad2f43afaf13) (text none))
  )
 )
)
