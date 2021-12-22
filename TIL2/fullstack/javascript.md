# JavaScript

- 웹 브라우저에서 실행 가능 - 웹브라우저가 자바스크립트의 인터프리터
- 개발자 도구의 console에서의 자바스크립트

```javascript
alert('hello javascript');
```

- URL 입력창에서의 자바스크립트

```javascript
javascript:alert('hello javascript')
```

- HTML 코드 내에서의 자바스크립트

```html
<script>자바스크립트 코드</script>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <script>
        alert('hello javascript')
    </script>
</head>
</head>
<body>

</body>
</html>
```

- HTML에서 외부에서 js 파일 가져오기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!--외부 자바 스크립트 코드 가져오기-->
    <script src='./js/script.js'>
    </script>
</head>
</head>
<body>

</body>
</html>
```



- node.js - 웹 브라우저 사용 x

```js
console.log('hello javascript')
```

```
C:\hw\workspace>node "c:\hw\workspace\js\script.js"
hello javascript    
```

basic_javascript.js

- vanilla javascript(순수 자바스크립트)
  - 자바스크립트만 이렇게 순수하게 사용할 일은 없음
  - 보통은 라이브러리를 사용함- vue, js, react, jquery, ...

```javascript
// 자바스크립트- 한 줄 주석
/*
멀티라인 주석- 여러 줄을 주석으로 처리 가능
*/

//변수의 정의와 선언이 따로따로 있음 -파이썬은 정의 안함

//변수의 선언
var var1; //var은 잘 쓰이지 않음
let var2; 

//변수 정의
var2 =10;
console.log(var2);     //10

//자료의 타입
console.log(typeof 10);//number
console.log(typeof 10.0); //number
console.log(typeof 'hello'); //문자열 타입 string
console.log(typeof true); //boolean

//파이썬에선 없는 타입
console.log(typeof null);  //object
console.log(typeof undefined); //undefined
console.log(typeof NaN);  //number
console.log(typeof Infinity); //number

//연산자
//몫연산은 없음
console.log(2+3); //5
console.log(2-3); //-1
console.log(2*3); //6
console.log(2/3); //0.6666666666666666
console.log(2%3); //2
console.log(2**3); //8

//파이썬에서는 없는 연산자
//증감 연산자
//전위식
let number =2;
console.log( ++number); //1씩 증가 3
console.log( --number); //1씩 감소 2
//전위식은 증감 먼저 하고 나머지 명령을 수행함

//후위식
number =2;
console.log(number++); //1씩 증가 2
console.log(number); //3
console.log(number--); //1씩 감소 3
console.log(number); //2
//후위식은 명령을 먼저 처리하고 나중에 1을 증감

// 비교 연산자
// 자바스크립트는 비교할 때 타입 고려 안함
console.log(1 == '1');  //true

//자바스크립트에서 타입까지 함께 고려하려면?
console.log(1 === '1');  //false

//논리연산자 - and, or, not -> &&, ||, !
console.log(true && false); //false
console.log(true || false); //true
console.log( !true );       //false

/* if (명제) {

}
*/

//윤년구하기
let year = 2000;
if ((year % 4==0) && (year% 100 !=0) || (year%400 ==0)) {
    console.log('윤년')
} else {
    console.log('평년')
}
//윤년

//몫 구하기
let q;
q=3/2;
q=parseInt(q);
console.log(q);   //1

//배열과 반복
//자바스크립트는 배열 타입 사용(파이썬의 리스트와 동일)

//let array=[];        // 1. 빈 배열 객체
//let array=Array();   // 2. Array 클래스의 생성자 이용해 객체 생성
let array=new Array(); //3. new 연산자 이용한 Array 객체 생성
array=[10,20,30,40];
console.log(array);
console.log(array[0]);


//파이썬의 append와 같은 역할 -push
array.push(50);
console.log(array);      //[10,20,30,40,50]
console.log(array[4]);   //50
//인덱스 범위를 넘어가는 경우
console.log(array[5]);  //undefined

//배열원소 추가 방법 + (그렇게 추천하진 않는 방법)
array[10]=100
console.log(array);      //[ 10, 20, 30, 40, 50, <5 empty items>, 100 ]


//자바스크립트는 배열을 파이썬의 dict처럼 사용 가능
//연관배열

let arr=[];
arr['first']=10;
console.log(arr);   //[ first: 10 ]


//for, while, for each

//파이썬의 for, while과는 다름

//1부터 10까지 반복
let i =1;         //초기값
while(i <=10) {   //조건
    console.log(i);
    i++;           //증감
/*
1
2
3
4
5
6
7
8
9
10
*/
    
//for(초기값;조건;증감) ; 한 줄에 표현
//동작은 while과 똑같이 동작
for (let i =1;i<=10;i++) {
    console.log(i);
}
    
//파이썬의 for과 동일한 역할을 하는 것 = for each
console.log(array);
for (let x of array) {
    console.log(x);
}
/*
[ 10, 20, 30, 40, 50, <5 empty items>, 100 ]
10
20
30
40
50
undefined
undefined
undefined
undefined
undefined
100
*/
    
//1부터 n까지의 총합
let n =20;
let sum=0;
for (let i =1 ; i<=n ; i++) {
    sum =sum +i;
}
console.log(sum);  //210
    
    
    
    
//함수의 기능은 파이썬과 동일
//'function' 키워드로 함수 정의

function func(a,b) {
    return a+b;
}
console.log(func(10,20))

//가변인자
function add() {
    //가변인자의 객체 =arguments'
    let sum=0;
    for(let i=0;i<arguments.length;i++){
        sum+=arguments[i];
    }
    return sum;
}
ret =add(1,2,3,4,5,6,7,8,9,10)
console.log(ret);  //55
    
    
    
//지역변수, 전역변수
let mem=10;
function func1() {
    let mem =20;
}
func1();
console.log(mem); //10
    
    
    
//디폴트 파라미터
function func2(a,b){
    console.log(a,b);
}
func2(); //undefined
    
function func2(a,b=2){
    console.log(a,b);
}
func2(); //undefined 2
    
    

//자바스크립트의 class
class Test{
    constructor(){
        console.log('생성자');
    }
}

obj= new Test();// 생성자

    

    
    
//자바스크립트의 클래스
class Person{
    //밑에 클래스 변수 아님
    //필드 선언 -> public과 private을 구분할 수 있음
    //속성 앞에 # 붙여서 private 설정, 외부에서 접근 불가능
    //name; //public
    #name
    #age; //private
    
    //생성자
    constructor(name, age) {
        //this=파이썬의 self
        // 따로 파라미터로 정의 안해도 항상 정의되어 있음
        this.name=name;
        this.age=age;
    };

    //class 내에서 메소드 정의할 때 'function' 키워드 생략함
    info() {
        console.log(this.name,this.age);
    }

}

//객체 생성
object = new Person('장동건',22);
object.info(); // 장동건 22
    
    
    
    
    
    
    //은닉성 # 사용
class Person{
    #name;
    #age;
    //생성자
    constructor(name, age) {
        //this=파이썬의 self
        // 따로 파라미터로 정의 안해도 항상 정의되어 있음
        this.name=name;
        this.age=age;
    };

    //calss 내에서 메소드 정의할 때 'function' 키워드 생략함
    info() {
        console.log(this.#name,this.#age);
    }

}

//객체 생성
object = new Person('장동건',22);
object.info();

//은닉성
object.#name='원빈';
object.info()    
    
/*장동건 22    
SyntaxError: Private field '#name' must be declared in an enclosing class */
    
    
    
    
    
  //정적 메소드  
class Person{
    #name;
    #age;
    //생성자
    constructor(name, age) {
        //this=파이썬의 self
        // 따로 파라미터로 정의 안해도 항상 정의되어 있음
        this.#name=name;
        this.#age=age;
    };
    
        //정적 메소드
    static staticMethod(){
        console.log(Person.nation) ;
    }


    //calss 내에서 메소드 정의할 때 'function' 키워드 생략함
    info() {
        console.log(this.#name,this.#age);
    }

}
    
//정적(static) 변수는 클래스 이름으로 접근 가능
console.log(Person.nation);

/*장동건 22
undefined
undefined*/
    
    
    
    
    
//getter setter

class Person{
    #name;
    #age;
    //생성자
    
    constructor(name, age) {
        //this=파이썬의 self
        // 따로 파라미터로 정의 안해도 항상 정의되어 있음
        this.#name=name;
        this.#age=age;
    };

    //정적 메소드
    static staticMethod(){
        console.log(Person.nation) ;
    }


    //getter와 setter
    get name(){
        return this.#name;
    }

    set name(name){
        this.#name=name;
    }

    //calss 내에서 메소드 정의할 때 'function' 키워드 생략함
    info() {
        console.log(this.#name,this.#age);
    }

}

//객체 생성
object = new Person('장동건',22);
object.info();

//은닉성
//object.#name='원빈';
//object.info()

//정적(static) 변수는 클래스 이름으로 접근 가능
console.log(Person.nation);
Person.staticMethod();


//getter와 setter 사용법
object.name='원빈';
console.log(object.name);
object.info(); //원빈 22

```

javascript_test.html -> 브라우저로 확인 , console에서 결과 확인 가능

```html
<!DOCTYPE html>
<html>
<head>
    <script type='text/javascript' src='../js/basic_javascript.js'></script>
</head>
<body>

</body>
</html>
```



### DOM(중요)

- Document Object Model, 문서 객체 모델
- 브라우저에서 보이는 문서를 하나의 객체로 다룸
- `document` 객체
  - 현재 브라우저에 보이는 문서는 하나의 도큐먼트 객체로 표현됨
  - 웹의 모든 내용을 전부 제어
  - 요소 - 추가, 수정, 삭제, 요소의 속성 추가, 수정, 삭제 등이 가능
  - 마우스 클릭, 키보드 입력 등의 이벤트에 대한 제어도 가능
- 요소(element)
  - 태그(=요소라고도 함), 속성, 내용(content)을 하나의 요소를 표현
  - DOM에선 각각의 요소를 계층적인 구조로 표현 

#### 요소의 선택

- 'document' 객체 내의 요소들을 다루는 API

  - `document.getElementByTagName('태그이름')`

  - `document.getElementById('id 속성')`

  - `document.getElementByClassName('class 속성')`

  - `document.querySelectAll('CSS 선택자')`

#### 계층구조를 이용한 접근

- DOM 구조에서는 각 요소들이 전부 하나의 객체가 됨
  - `document.요소이름`
- 각 노드와의 관계
  - parentNode : 현재노드의 상위노드
  - childNode : 자식
  - firstChild : 첫번째 자식
  - lastChild : 마지막 자식
  - nextSibling : 다음 형제 노드
  - previousSibling : 이전 형제 노드



###  BOM(중요)

- Browser Object Model
- 브라우저 또한 객체란 뜻
- `window` 객체
  - **history** : 방문했던 페이지 정보
    - `window.history.back()` : 이전 페이지<-
    - `window.history.forward()` : 다음 페이지->
  - **location** : 현재 열려있는 페이지
    - `window.location.href` : 현재 열려있는 페이지 URL



### 카운터 만들기 실습

counter.html

```html
<!DOCTYPE html>
<html>
  <head>

  </head>

  <body>
    <h2 id='number'>0</h2>
    <div>
      <button id='increase'>+1</button>
      <button id='decrease'>-1</button>
    </div>

    <script>
        let number = document.getElementById('number');
        let up = document.getElementById('increase');
        let down = document.getElementById('decrease');
  
        //요소에 이벤트 달기
        up.onclick = function() {
            let count = number.innerText;
            count = parseInt(count);
            number.innerText= ++count;
        };

        down.onclick = function() {
            let count = number.innerText;
            count = parseInt(count); // 문자열을 정수로
            number.innerText= --count;
        };
      </script>
  </body>
</html>
```

