@startuml
' hide the spot
hide circle

' avoid problems with angled crows feet
skinparam linetype ortho

entity "1. Problem Formulation" as e01 {
  Input : problem to be answered
  --
  Method : literature review
  --
  Output : research questions
}

entity "2. Literatur Study" as e02 {
  Input : research questions, relevant research
  --
  Method : //compare//, //contrast//, //synthesize//, //summarize//, //criticize//
  --
  Output : theoretical basis and literature review
}

entity "3. Application Design and Implementation" as e03 {
  Input : application architecture design
  --
  Method : application development using programming
  --
  Output : working applications and architecture design
}

entity "4. Performance Evaluation and Analysis" as e04 {
  Input : working applications, test scenarios
  --
  Method : experimentation, observation, quantitative analysis
  -- 
  Output : performance measurement results of all test scenarios
}

entity "5. Inference" as e05 {
  Input : evaluation results, research questions
  --
  Method : evaluation analysis
  --
  Output : conclusions and future research
}


e01 -> e02
e02 -d-> e03
e03 -up-> e02
e03 -d-> e04
e04 -> e05

@enduml

