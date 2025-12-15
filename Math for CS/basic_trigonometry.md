---
id: basic_trigonometry
aliases: []
tags: []
---
j
# Definition of Sine and Cosine Functions

$$
\begin{aligned}
\sin \theta = \frac{opposite side}{hypothenuse} = \frac{a}{h} \\
\cos \theta = \frac{adjacent side}{hypothenuse} = \frac{b}{h}
\end{aligned}
$$


in Figure 1.35
![sin_cos.png|200](assets/imgs/sin_cos.png)

## Definition of $\sin\theta$ and $\cos\theta$

원 $x^2 + y^2 = 1$에 대하여, 

$$
\begin{aligned}
\sin\theta = y\\
\cos\theta = x
\end{aligned}
$$
![figure_1_40.png|200](assets/imgs/figure_1_40.png)

## 삼각함수의 항등식

원 $x^2 + y^2 = 1$의 $x$, $y$에 $\sin$, $\cos$를 대입하면 그대로 

$$
\sin^2\theta + \cos^2\theta = 1
$$

### addition formula
삼각함수의 덧셈 공식은 **삼각함수의 값을 더하거나 빼는 형태**를 단순화하는 데 유용한 공식입니다. 가장 기본적인 공식은 **사인, 코사인, 탄젠트의 덧셈·뺄셈 공식**입니다.

---

**1. 사인 덧셈·뺄셈 공식**
$$
\sin (A + B) = \sin A \cos B + \cos A \sin B
$$

**2. 코사인 덧셈·뺄셈 공식**
$$
\cos (A + B) = \cos A \cos B - \sin A \sin B
$$

#### double angle formula
$$
\begin{align}
    \sin(\theta + \phi) &= \sin\theta \cos\phi + \cos\theta \sin\phi \tag{3} \\
    \cos(\theta + \phi) &= \cos\theta \cos\phi - \sin\theta \sin\phi. \tag{4}
\end{align}
$$

**3. 탄젠트 덧셈·뺄셈 공식**
$$
\tan (A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}
$$
   $$
   e^{\pi i}=-1
    $$  
> [!PROOF]- proof of the trigonometric addition formulas using **Euler's formula**
> 1. **State the Addition Formulas**  
>    The formulas we want to prove are:  
>    - **Sine Addition Formula** :  
>      $$
>      \sin(a+b)=\sin a\,\cos b+\cos a\,\sin b
>      $$  
>    - **Cosine Addition Formula** :  
>      $$
>      \cos(a+b)=\cos a\,\cos b-\sin a\,\sin b
>      $$
> 
> 2. **Recall Euler’s Formula**  
>    **Euler's formula** :  
>    $$
>    e^{i\theta}=\cos\theta+i\sin\theta
>    $$  
>    holds for any real number $\theta$.
> 
> 3. **Apply Euler’s Formula to $a$ and $b$**  
>    For angles $a$ and $b$, we have:
>    $$
>    e^{ia}=\cos a+i\sin a,\quad e^{ib}=\cos b+i\sin b.
>    $$
> 
> 4. **Express $e^{i(a+b)}$ in Two Ways**  
>    On one hand, by Euler’s formula:
>    $$
>    e^{i(a+b)}=\cos(a+b)+i\sin(a+b).
>    $$  
>    On the other hand, using the property of exponents:
>    $$
>    e^{i(a+b)}=e^{ia}\cdot e^{ib}=(\cos a+i\sin a)(\cos b+i\sin b).
>    $$
> 
> 5. **Expand the Product**  
>    Multiply out the right‐hand side:
>    $$
>    (\cos a+i\sin a)(\cos b+i\sin b)=\cos a\,\cos b+i\cos a\,\sin b+i\sin a\,\cos b+i^2\sin a\,\sin b.
>    $$  
>    Since $i^2=-1$, this becomes:
>    $$
>    \cos a\,\cos b-\sin a\,\sin b+i(\cos a\,\sin b+\sin a\,\cos b).
>    $$
> 
> 6. **Equate Real and Imaginary Parts**  
>    Since the two expressions for $e^{i(a+b)}$ must be equal, their real and imaginary parts are equal:
>    
>    - **Real part**:
>      $$
>      \cos(a+b)=\cos a\,\cos b-\sin a\,\sin b.
>      $$
>    
>    - **Imaginary part**:
>      $$
>      \sin(a+b)=\cos a\,\sin b+\sin a\,\cos b.
>      $$
> 
> This completes the proof using **Euler's formula**.

> [!PROOF]- proof using derivatives and the uniqueness of solutions to differential equations
> 
> Suppose we wish to prove that for all real numbers $x$ and a fixed angle $a$ the following formulas hold:
>   
> $$
> \begin{aligned}
> \sin(x+a) &= \sin x\,\cos a+\cos x\,\sin a,\\[1mm]
> \cos(x+a) &= \cos x\,\cos a-\sin x\,\sin a.
> \end{aligned}
> $$
> 
> We proceed as follows:
> 
> ---
> 
> **1. Define the Candidate Functions**
> 
> Let
> 
> $$
> u(x)=\cos(x+a) \quad\text{and}\quad v(x)=\sin(x+a).
> $$
> 
> Because sine and cosine are known to be differentiable and satisfy the differential equations
> 
> $$
> \frac{d}{dx}\cos x = -\sin x \quad\text{and}\quad \frac{d}{dx}\sin x = \cos x,
> $$
> 
> we have
> 
> $$
> \begin{aligned}
> u'(x) &= -\sin(x+a)= -v(x),\\[1mm]
> v'(x) &= \cos(x+a)= u(x).
> \end{aligned}
> $$
> 
> Also, the initial values at $x=0$ are
> 
> $$
> u(0)=\cos a,\quad v(0)=\sin a.
> $$
> 
> ---
> 
> **2. Define Functions Based on the Addition Formulas**
> 
> Now define functions
> 
> $$
> U(x)=\cos a\,\cos x-\sin a\,\sin x,\quad V(x)=\sin a\,\cos x+\cos a\,\sin x.
> $$
> 
> We will show that $U(x)$ and $V(x)$ satisfy the same differential equations and initial conditions as $u(x)$ and $v(x)$, respectively.
> 
> Differentiate $U(x)$:
> 
> $$
> \begin{aligned}
> U'(x) &= -\cos a\,\sin x-\sin a\,\cos x\\[1mm]
>       &= -\Bigl(\sin a\,\cos x+\cos a\,\sin x\Bigr)\\[1mm]
>       &= -V(x).
> \end{aligned}
> $$
> 
> Differentiate $V(x)$:
> 
> $$
> \begin{aligned}
> V'(x) &= -\sin a\,\sin x+\cos a\,\cos x\\[1mm]
>       &= \cos a\,\cos x-\sin a\,\sin x\\[1mm]
>       &= U(x).
> \end{aligned}
> $$
> 
> The initial conditions are also readily checked:
> 
> $$
> \begin{aligned}
> U(0) &= \cos a\cdot\cos 0-\sin a\cdot\sin 0 = \cos a,\\[1mm]
> V(0) &= \sin a\cdot\cos 0+\cos a\cdot\sin 0 = \sin a.
> \end{aligned}
> $$
> 
> ---
> 
> **3. Conclude by Uniqueness**
> 
> Since both pairs $\bigl(u(x),v(x)\bigr)$ and $\bigl(U(x),V(x)\bigr)$ satisfy the same system of first‑order differential equations
> 
> $$
> \begin{cases}
> y'(x)=-z(x),\\[1mm]
> z'(x)=y(x),
> \end{cases}
> $$
> 
> with identical initial conditions at $x=0$, the uniqueness theorem for ordinary differential equations implies that
> 
> $$
> u(x)=U(x)\quad\text{and}\quad v(x)=V(x)\quad\text{for all }x.
> $$
> 
> That is,
> 
> $$
> \begin{aligned}
> \cos(x+a)&=\cos a\,\cos x-\sin a\,\sin x,\\[1mm]
> \sin(x+a)&=\sin a\,\cos x+\cos a\,\sin x.
> \end{aligned}
> $$
> 
> These are exactly the trigonometric addition formulas.
> 
> ---
> 
> **Summary**
> 
> Using derivatives and the uniqueness of solutions to differential equations, we have shown that the functions
> 
> $$
> \sin(x+a)=\sin x\,\cos a+\cos x\,\sin a\quad \text{and}\quad \cos(x+a)=\cos x\,\cos a-\sin x\,\sin a
> $$
> 
> hold for all real $x$ and $a$.
> 
> This completes the derivative-based proof of the trigonometric addition formulas.

---

이 공식들은 삼각함수를 더하거나 빼야 할 때 매우 유용하며, **삼각 방정식, 삼각 함수 그래프 변환, 물리학(파동) 등** 다양한 분야에서 활용됩니다.  


