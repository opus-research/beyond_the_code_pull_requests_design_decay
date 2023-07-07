---

title: Beyond the Code - Investigating the Effects of Pull Request Conversations on Design Decay
---

# Paper Title

Beyond the Code - Investigating the Effects of Pull Request Conversations on Design Decay

# Authors

Caio Barbosa, Anderson Uchôa, Daniel Coutinho, Wesley K. G. Assunc ̧ Anderson Oliveira, Alessandro Garcia, Baldoino Fonseca, Matheus Rabelo, José Eric Coelho, Eryka Carvalho, Henrique Santos

# Abstract

Background: Code development is done collaboratively in platforms such as GitHub and GitLab, following a pull-based development model. In this model, developers actively communicate and share their knowledge through conversations. Pull request conversations are affected by social aspects such as communication dynamics among developers, discussion content, and organizational dynamics. Despite prior studies indicating that social aspects indeed impact software quality, it is still unknown to what extent social aspects influence design decay during software development. Thus, since social aspects are intertwined with design and implementation decisions, there is a need for investigating how social aspects contribute to avoiding, reducing, or accelerating design decay.
Aims: To fill this gap, we performed a study aimed at investigating the effects of pull request conversation on design decay. 

Method: We investigated 10,746 pull request conversations from 11 open-source systems, characterizing in terms of three different social aspects: discussion content, organizational and communication dynamics. We considered 18 social metrics to these three social aspects, and analyzed how they associate with design decay. We used a statistical approach to assess which social metrics are able to discriminate between impactful and unimpactful pull requests. Then, we employed a multiple logistic regression model to evaluate the influence of each social metric per social aspect in the presence of each other on design decay. Finally, we also observed how the combination of all social metrics influences the design decay. 

Results: Our findings reveal that social metrics related to the size and duration of a discussion, the presence of design-related keywords, the team size, and gender diversity can be used to discriminate between design impactful and unimpactful pull requests. Organizational growth and gender diversity prevent decay. Each software community has its unique aspects that can be used to detect and prevent design decay. Also, design improvements can be accomplished by timely feedback, engaged communication, and design-oriented discussions with the contribution of multiple participants who provide significant comments. Conclusion: The social aspects related to pull request conversations are useful indicators of design decay.

# Replication Package

The data for the statistical methods and the scripts for running the analysis can be found on the following repository on [GitHub](https://github.com/opus-research/beyond_the_code_pull_requests_design_decay).

# User Classification Method

In order classify the developers on Newbies, Contributors, Core Devs, we used the GitHub API tag [author_association](https://docs.github.com/en/graphql/reference/enums#commentauthorassociation).

We classified each developer considering the following:

| Classification | Tags | 
|:---------------|:-----|
| User           | FIRST_TIMER, FIRST_TIME_CONTRIBUTOR, NONE |
| Contributor    | CONTRIBUTOR, COLLABORATOR |
| Core Developer | MEMBER, OWNER |

# Design Symptoms Descriptions

| Class-level | Description |
|:-------------|:------------|
|	Abstract Function Call From Constructor	|	A constructor that calls an abstract method	|
|	Complex Conditional	|	A conditional statement that is complex	|
|	Complex Method	|	A method that has high cyclomatic complexity |
|	Empty Catch Block	|	A catch block of an exception that is empty	|
|	Long Identifier	|	An identifier that is excessively long	|
|	Long Method	|	A method that is too long to understand	|
|	Long Parameter List	|	A method that accepts a long list of parameters	|
|	Long Statement	|	A statement that is excessively long|
|	Magic Number	|	When an unexplained number is used in an expression A switch statement that does not contain a default case	|
|	Missing Default	|	A switch statement that does not contain a default case	|

| Method-level | Description |
| :-------------------------------------- | :-------------------------------------------|
|	Broken Hierarchy	|	A supertype and its subtype that conceptually do not share an "is a" relationship		|
|	Broken Modularization	|	When data and/or methods that should have been into a single abstraction are spread across multiple abstractions		|
|	Cyclic Dependent Modularization	|	When two or more abstractions depend on each other directly or indirectly		|
|	Cyclic Hierarchy	|	A supertype in a hierarchy that depends on any of its subtypes		|
|	Deep Hierarchy	|	An inheritance hierarchy that is excessively deep		|
|	Deficient Encapsulation	|	The accessibility of one or more members of an abstraction is more permissive than actually required		|
|	Hub Like Modularization	|	An abstraction that has dependencies with a large number of other abstractions		|
|	Imperative Abstraction	|	When an operation is turned into a class		|
|	Insufficient Modularization	|	An abstraction that has not been completely decomposed		|
|	Missing Hierarchy	|	When a design segment uses conditional logic instead of polymorphism		|
|	Multifaceted Abstraction	|	An abstraction that has more than one responsibility assigned to it		|
|	Multipath Hierarchy	|	A subtype that inherits both directly as well as indirectly from a supertype		|
|	Rebellious Hierarchy	|	A subtype that rejects the methods provided by its supertype(s)		|
|	Unexploited Encapsulation	|	A client class that uses explicit type checks instead of exploiting the variation in types already encapsulated within a hierarchy		|
|	Unnecessary Abstraction	|	An abstraction that is actually not needed in the system		|
|	Unutilized Abstraction	|	An abstraction that is left unused		|
|	Wide Hierarchy	|	An inheritance hierarchy that is too wide		|
