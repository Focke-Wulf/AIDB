#                   Deepdive 框架下NLP神经网络测试

> ​					Reported by JUNWEN XIE
>
> ​                                                    国云数据  

## Deepdive-简介

### 背景相关：

暗数据（Dark data) : 数据需要被转化成知识，需要分析或者被记录，否则就是暗数据状态，比如企业日志，工作汇报等等，这些数据往往只是被利用一次，并且需要得到良好的保存不然可能会带来风险，暗数据在国家安全，商业机密，个人信息等方面具有潜在价值和风险的资源。暗数据另一个特性是结构性和非结构性并存的状态，数据可能是表格，文本，图片等等一系列信息表现形式，非结构性数据，很难被加以利用，这也是为何暗数据无法得到有效利用的原因之一。

Deepdive 是一种用来处理从 实例->推论结果 这么一个复杂的关系网络的开源项目平台，Deepdive 能够将非结构化的数据变成结构化的结果并且保存在数据库中用来做数据分析.

#### Deepdive能做什么？

Deepdive 能提取实例，集成和预测问题，他可以提供点到点的数据流水线，开发者可以自己的系统当中通过脚本或者手动操作对含有噪声和不精确的数据进行处理和分析，该平台能够解决大规模统计和推断相关的问题。

##Deepdive-配置

在Linux系统下 可以直接下载配置集成的好的Deepdive 平台

```Shell
bash <(curl -fsSL git.io/getdeepdive)
```

Deepdive 需要配置环境变量来调用本体程序，经过测试，变量配置在 ~/.bashrc 文件中可以达到效果远程的话需要~/.bash_profile 中配置路径

```shell
#这里Deepdive默认安装在local/bin文件夹中
export PATH=~/local/bin:"$PATH"
```

Deepdive 需要配合SQL数据库，在这里强烈推荐PSQL数据库，管理方便，效率高,在这里我们安装官方推荐配置的PSQL数据库，在Bash下运行：

```shell
bash <(curl -fsSL git.io/getdeepdive) postgres
```

配置postgres 这里做个记录，系统默认用户名是 postgres 可以直接用 ps postgres 登录，这里要设置用户密码，否则有潜在安全问题，必须再增加一个用户，提供给Deepdive来上传和下载数据，一般新增用户是系统名，在Deepdive中，会直接用当前系统用户登录使用数据库。另外为了方便管理数据库，这里使用 pgAdmin4 在python环境下的可视化数据库管理程序用来检测分析结果.

​                                      **postgres配置 命令放在附录中**

 

## Deepdive-结构

开发一款Deepdive 应用，需要从最基本结构入手了解这个平台是如何运行的，作为Deepdive的开发者，需要掌握什么方面的内容，这篇报告主要内容则是实践和测试如何从一个最初的Deepdive 框架，并且开发和设计实现机器学习分析平台。

PS： 由于网上中文资料较少，并且没有研究其内核方面，对于该平台的结构，将会是重点关注的方向。

文件结构：

|  /bin  |  /etc   | / lib | /mindbender |   /util    |
| :----: | :-----: | :---: | :---------: | :--------: |
| 主要项目文件 | bash 配置 |  环境包  |     工具包     |  命令shell   |
| 需要自定义  | 简单的默认配置 | 自带配置  |   可以借鉴使用    | Deepdive内核 |

/bin 目录下默认只有 *Deepdive* *mindbender* *ddlog* 三个shell  脚本文件，其他目录需要自己创建，在官网样例中给了一个参考项目，里面不少工具可以现成导入使用，不过有一些局限性，在这里我们自己单独建立项目结构，入手了整个文本处理流程，用来逐步测试学习。

Deepdive 需要 /bin 文件下至少有一下几个文件存在.

1. app.ddlog 这是一个类似MATLAB 语言用来搭建真个项目的流程，我们可以叫做模板，定义结构的文件，里面的参数将决定了我们产生数据的格式，关联性等,在里面定义函数调用自己定义的算法可以推算，预测最后结果，是最主要的文件。

2. db.url 文件定义了数据库的链接地址和数据库名称，一旦定义好，所有数据将被整理在当前数据库下.

3. /input 这是一个input 文件夹，用来存放导入数据,可以高度自定义,灵活运用，推荐使用 tsv 格式数据，csv无法区分复杂文档中符号问题.

4. /run 这个文件夹是自动生成的，里面存放了log文件历史处理信息，便于查阅，有意思的是，还能自动根据项目设计流程生成流程图，方便以后设计，生成该文件需要 deepdive compile 编译当前所有文档，每一次修改/bin 文件夹里的设置文档都需要 运行deepdive compile，不然可能无法正常运行.

5. /udf 这个文件是存放工具包的，Deepdive 在演示项目例子中集成了一些工具（bazaar）用来处理学习文本，类似parser 这样的集成包利用斯坦福的nlp神经网络算法添加了可以直接从数据库读取数据处理数据返回数据的功能,在这里我们根据自己需求搭建自己工具处理环境，我手动添加了处理中文的模块，所以该平台现在能良好支持中文处理，之后可以在多核 并行，云计算集群等都能运行提高机器学习效率。

6. 剩下其余文件夹都可以自己定义其各个功能。

   ​

## Deepdive - 项目建立

本测试项目目的做一些简单的功能测试学习相关内容，并且根据需求逐渐添加功能。

### 1. 定义db.url 文件放在 /bin 目录下，  







## 





### 2. app.ddlog 文件 

app.ddlog 文件被用来定义数据结构和数据关系的文件，系统中脚步通过读取该文件所以定义的结构创建数据中的表并导入和到处数据，该文件还能使用操作函数调用外部文件包对数据进行处理。总结，app.ddlog 是deepdive进行自然语言学习最重要的部分，app.ddlog 的结构和函数定义，决定了正个deepdive的流水线操作





####2.1 '@' Mindbender and deepdive annotations

在deepdive中需要机器能够理解数据之间的关系，annotations 注解器用来定义表中每一列之间的数据关系，这样才能清楚的对文本内容进行查找和标注。表中每一列的关联性被标记为 @key 和 @references. （其实就是SQL里的reference_Key)

举例： 文章实体 entity  （可以理解为经过词性标注后拆分过的表）和 文档 document（原始文章所储存的表）的关联注解标注需要：

```MATLAB
document( @key  id text, ... ).
entity( ...,  @references(relation="documents", column="id")  doc_id text ).
```

其中entity 中的 doc_id 就会和 document 中的 id 关联在一起，以表明，实体中的句子被切分开来 依然属于同一篇文章。

####2.2 注解关系数据的关联关系

所有可浏览的关联数据都被标注为 @source 和 @extraction

#####@references 和 @key 是注解 嵌套在表与表中的某些数据列之间的关系。

#####在注解为 @extraction 表里需要有 @references 的表列 链接到@source 表中

#####每一列中的数据均可被查找

#####注解为 @searchable 的表列会被高亮展示

#####注解为@navigable  和 @searchable 可以被用来多面导向功能。



使用mindbender 用来作数据结果测试

```shell
mindbender search update
```

```shell
mindbender search gui

```

 浏览器 打开<http://localhost:8000/#/search>

DDlog 中一些常用的模式定义数据关系

1. Relation that holds source (input) data
   - text corpus with NLP markups
   - dictionaries, controlled vocabularies
   - ontologies, knowledge bases, known relationships
2. Relation that holds extractions
   - candidates
   - mentions, relationship mentions, entity links
   - features
   - supervision labels
3. Relation that holds predictions (random variables)
   - whose expectation predicted by DeepDive

例如：

1. Source
   - `articles`
   - `sentences`
   - `spouse_dbpedia`
2. Extraction
   - `person_mention`
   - `spouse_candidate`
   - `spouse_feature`
   - `spouse_label`
3. Prediction
   - `has_spouse`

DDlog 可以允许在注解关联声明中添加参数 比如@name（这里放参数） 参数可选 @tag ，也是一种可行的注解声明，另外，参数可以是命名的参数也可以是非命名的参数。例如

`@foo(1,"two", 3.45)`

`@bar(number=1,string="two",double=3.45)`

参数类型可以为 integers, floating point numbers, or strings.

##### 一些常用的注解

解释详见：

http://deepdive.stanford.edu/browsing

#####`@key` columns

#####`@references(relation, [column], [alias])` columns

#####`@extraction([label])` relations

#####`@searchable([relation, ...])` columns

#####`@source([label])` relations

#####`@navigable([relation, ...])` columns

#### 2.3 app.ddlog 定义数据形式

```matlab
relation_name(
  column1_name  column1_type,
  column2_name  column2_type,
  ...
).
```

```matlab
 article(  
	 id     int,
 	length int,
 	author text,
 	words  text[]
 ).
```



#### 2.4 常用推导规则

在关联性表里，通常需要知道各个数据之间的派生关系

```matlab
Q(x, y) :- R(x, y), S(y).
```

其中Q 是关联好的数据表名称 比如叫sentence ， R 或者 S 可以使谓词连词，或者用来定义变量的条件 例如：

```matlab
a(k int).
b(k int, p text, q text, r int).
c(s text, n int, t text).

Q("test", f(123), id) :- a(id), b(id, x,y,z), c(x || y,10,"foo").

R(TRUE, power(abs(x-z), 2)) :- a(x), b(y, _, _, _).

S(if l > 10 then TRUE
else if l < 10 then FALSE
else NULL end) :- R ( _, l).
```

Here tuples of string literal "text", a function `f` applied to 123, and `id` bound by the body of the rule are added to relation `Q`. Then, we add to the relation `R` the boolean `TRUE` and operations from variables in `a` and `b`. Finally, we fill out the relation `S` by a condition value according to the second variable in `R`.







































## 附录 

**常用解释**

斯坦福 NLP词性分类

**词性解释**

CC: conjunction, coordinatin 表示连词
CD: numeral, cardinal 表示基数词
DT: determiner 表示限定词
EX: existential there 存在句
FW: foreign word 外来词
IN: preposition or conjunction, subordinating 介词或从属连词
JJ: adjective or numeral, ordinal 形容词或序数词
JJR: adjective, comparative 形容词比较级
JJS: adjective, superlative 形容词最高级
LS: list item marker 列表标识
MD: modal auxiliary 情态助动词
**NN**: noun, common, singular or mass
NNS: noun, common, plural
NNP: noun, proper, singular
NNPS: noun, proper, plural
PDT: pre-determiner 前位限定词
POS: genitive marker 所有格标记
PRP: pronoun, personal 人称代词
PRP$: pronoun, possessive 所有格代词
RB: adverb 副词
RBR: adverb, comparative 副词比较级
RBS: adverb, superlative 副词最高级
RP: particle 小品词
SYM: symbol 符号
TO:"to" as preposition or infinitive marker 作为介词或不定式标记
UH: interjection 插入语
VB: verb, base form
VBD: verb, past tense
VBG: verb, present participle or gerund
VBN: verb, past participle
VBP: verb, present tense, not 3rd person singular
VBZ: verb, present tense,3rd person singular
WDT: WH-determiner WH限定词
WP: WH-pronoun WH代词
WP$: WH-pronoun, possessive WH所有格代词
WRB:Wh-adverb WH副词

**句法分析（句法树）
**

ROOT：要处理文本的语句
IP：简单从句
NP：名词短语
VP：动词短语
PU：断句符，通常是句号、问号、感叹号等标点符号
LCP：方位词短语
PP：介词短语
CP：由‘的’构成的表示修饰性关系的短语
DNP：由‘的’构成的表示所属关系的短语
ADVP：副词短语
ADJP：形容词短语
DP：限定词短语
QP：量词短语
NN：常用名词
**NR**：固有名词：表示仅适用于该项事物的名词，含地名，人名，国名，书名，团体名称以及一事件的名称等。
NT：时间名词
PN：代词
VV：动词
VC：是
CC：表示连词
VE：有
**VA**：表语形容词
AS：内容标记（如：了）
VRD：动补复合词
CD: 表示基数词
DT: determiner 表示限定词
EX: existential there 存在句
FW: foreign word 外来词
IN: preposition or conjunction, subordinating 介词或从属连词
JJ: adjective or numeral, ordinal 形容词或序数词
JJR: adjective, comparative 形容词比较级
JJS: adjective, superlative 形容词最高级
LS: list item marker 列表标识
MD: modal auxiliary 情态助动词
PDT: pre-determiner 前位限定词
POS: genitive marker 所有格标记
PRP: pronoun, personal 人称代词
RB: adverb 副词
RBR: adverb, comparative 副词比较级
RBS: adverb, superlative 副词最高级
RP: particle 小品词 
SYM: symbol 符号
TO:”to” as preposition or infinitive marker 作为介词或不定式标记 
WDT: WH-determiner WH限定词
WP: WH-pronoun WH代词
WP$: WH-pronoun, possessive WH所有格代词
WRB:Wh-adverb WH副词
**关系表示
**abbrev: abbreviation modifier，缩写
acomp: adjectival complement，形容词的补充；
advcl : adverbial clause modifier，状语从句修饰词
advmod: adverbial modifier状语
agent: agent，代理，一般有by的时候会出现这个
amod: adjectival modifier形容词
appos: appositional modifier,同位词
attr: attributive，属性
aux: auxiliary，非主要动词和助词，如BE,HAVE SHOULD/COULD等到
auxpass: passive auxiliary 被动词
cc: coordination，并列关系，一般取第一个词
ccomp: clausal complement从句补充
complm: complementizer，引导从句的词好重聚中的主要动词
conj : conjunct，连接两个并列的词。
cop: copula。系动词（如be,seem,appear等），（命题主词与谓词间的）连系
csubj : clausal subject，从主关系
csubjpass: clausal passive subject 主从被动关系
dep: dependent依赖关系
det: determiner决定词，如冠词等
dobj : direct object直接宾语
expl: expletive，主要是抓取there
infmod: infinitival modifier，动词不定式
iobj : indirect object，非直接宾语，也就是所以的间接宾语；
mark: marker，主要出现在有“that” or “whether”“because”, “when”,
mwe: multi-word expression，多个词的表示
neg: negation modifier否定词
nn: noun compound modifier名词组合形式
npadvmod: noun phrase as adverbial modifier名词作状语
nsubj : nominal subject，名词主语
nsubjpass: passive nominal subject，被动的名词主语
num: numeric modifier，数值修饰
number: element of compound number，组合数字
parataxis: parataxis: parataxis，并列关系
partmod: participial modifier动词形式的修饰
pcomp: prepositional complement，介词补充
pobj : object of a preposition，介词的宾语
poss: possession modifier，所有形式，所有格，所属
possessive: possessive modifier，这个表示所有者和那个’S的关系
preconj : preconjunct，常常是出现在 “either”, “both”, “neither”的情况下
predet: predeterminer，前缀决定，常常是表示所有
prep: prepositional modifier
prepc: prepositional clausal modifier
prt: phrasal verb particle，动词短语
punct: punctuation，这个很少见，但是保留下来了，结果当中不会出现这个
purpcl : purpose clause modifier，目的从句
quantmod: quantifier phrase modifier，数量短语
rcmod: relative clause modifier相关关系
ref : referent，指示物，指代
rel : relative
root: root，最重要的词，从它开始，根节点
tmod: temporal modifier
xcomp: open clausal complement
xsubj : controlling subject 掌控者