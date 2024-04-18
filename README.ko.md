# 수학 함수 및 볼륨 계산기
> 이 프로그램은 Tkinter 라이브러리를 기반으로 개발된 GUI(그래픽 사용자 인터페이스) 응용 프로그램입니다.이것은 수학 함수를 그리고, 함수의 적분을 계산하고, 사용자의 선택에 따라 지정된 축을 중심으로 함수를 회전하여 얻은 3차원 부피를 계산하는 데 사용됩니다.
# #
# # # 특징
- 수학 함수를 입력하고 함수의 도메인을 지정할 수 있습니다.
- 프로그램은 원본 함수와 그 적분을 그리고 적분 결과를 표시합니다.
- 스풀 회전 함수를 통해 얻은 고체 볼륨을 계산할지 여부를 선택할 수 있습니다.
- X축 또는 Y축을 중심으로 회전할 축을 선택할 수 있습니다.
- 프로그램은 사용자의 선택에 따라 회전된 3D 볼륨을 그리고 계산 결과를 표시합니다.
# #
용법
# # # # 전제 조건:
-Python 3.x
-NumPy
-Matplotlib
-Sympy
-Tkinter
# # # 단계:
1. 코드를 복사하여 파이썬 IDE에 붙여넣습니다.
2. 코드를 실행합니다.
3. GUI에서 다음을 입력합니다.
- 함수 표현식 (예: x**2)
- 포인트 범위의 시작 값 (예: 0)
- 포인트 범위의 최종 값 (예: 1)
- (선택 사항) X축 또는 Y축 주위의 볼륨 계산을 선택합니다.
4. 함수와 포인트 그리기 버튼을 클릭합니다.
   
# # # # 코드 설명:
- 이 코드는 함수를 입력하고 적분과 볼륨을 계산할 수 있는 GUI 응용 프로그램을 만듭니다.
- X축 또는 Y축 주위의 볼륨을 계산하도록 선택할 수 있습니다.
- 코드는 Sympy를 사용하여 함수를 확인하고 통합을 수행합니다.
- 함수, 적분 및 볼륨을 그리기 위해 Matplotlib 및 Tkinter를 사용합니다.
인스턴스
함수 x^2의 포인트를 그리고 x축 주위의 볼륨을 계산하려면 다음 절차를 따르십시오.
1. 함수 표현식 x**2를 입력합니다.
2. 포인트 범위 0의 시작 값을 입력합니다.
3. 포인트 범위 1의 종료 값을 입력합니다.
4. X축 주위 옵션을 선택합니다.
5. 함수와 포인트 그리기 버튼을 클릭합니다.
결과
프로그램은 함수 x^2, 적분 및 x축 주위의 볼륨을 그립니다.볼륨 결과가 GUI에 표시됩니다.
# #
# # # 코드 구조
프로그램의 코드 구조는 다음과 같습니다.
1. 필요한 라이브러리 및 모듈 가져오기
-**tkinter 라이브러리**: GUI 인터페이스를 만드는 데 사용됩니다.
-**numpy 라이브러리 **: 숫자 계산 및 배열 연산에 사용됩니다.
- * * matplotlib 라이브러리 * * 도면을 그릴 때 사용합니다.
-**mpl_toolkits.mpt3d 모듈 **: 3D 도면을 그릴 때 사용됩니다.
- ** 기호 라이브러리 **: 기호 계산에 사용됩니다.
-**ttk** 테마 Tkinter 위젯용
2. 함수 plot_volume_around_aaxis를 정의합니다.
- 이 함수는 x축 또는 y축을 중심으로 함수를 회전하여 생성된 솔리드의 볼륨을 계산하고 Matplotlib을 사용하여 플롯합니다.
3. 이벤트 처리기 함수 on_plot_hover 정의:
- 이 함수는 드로잉에서 서스펜션 이벤트를 처리하고 서스펜션 점의 좌표를 표시하는 데 사용됩니다.
    
4. 함수 plot_function_integral_volume 정의:
- Plot function and Integral(함수 및 적분 그리기) 버튼을 클릭하면 이 함수가 호출됩니다.
- 기능, 범위 및 회전 축에 대한 사용자 입력을 읽어들입니다.
- 원래 함수와 해당 포인트를 그리고 Matplotlib을 사용하여 포인트 결과를 표시합니다.
- 사용자가 볼륨 계산 옵션을 선택하면 plot_Volume_around_aaxis 함수가 호출되어 볼륨을 계산하고 그립니다.
5. Tkinter 창을 만들고 속성을 설정합니다.
- Tk 창 객체를 만듭니다.
- 창 제목, 크기 및 스타일을 설정합니다.
- 작은 부품을 수용하고 배치를 구성하는 마스터 프레임을 작성합니다.
      
6. Tkinter 위젯 만들기:
- 사용자 입력을 위한 레이블 만들기, 입력 필드, 확인란 및 버튼
- 위젯을 기본 프레임에 격자선화합니다.
      
7. 레이아웃 및 이벤트 처리 구성:
- columnconfigure 및 rowconfigure를 사용하여 마스터 프레임의 레이아웃을 구성합니다.
- canvas.mpl_connect를 사용하여 이벤트 처리기 함수를 Matplotlib 드로잉에 바인딩합니다.
      
8. Tkinter 주 이벤트 루프를 실행합니다.
- Tkinter 이벤트 루프를 시작하여 GUI 창을 표시하고 사용자 상호 작용을 처리합니다.
      
# #
# # # 그래픽 요약 * (이 소프트웨어는 어떻게 생겼습니까?)

<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/5.png"/>

<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/6.png"/>

<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/8.png"/>

# #
# # # 애플리케이션 개발 프로세스의 유형입니다.
민첩했어
# #
# # # 우리가 (민첩하게) 선택한 이유는 무엇입니까?
배경
> 우리는 강력한 수학 도구가 부족한 상황에서 학생과 교육자가 복잡한 수학 개념을 쉽게 시각화하고 이해할 수 있도록 강력하고 사용하기 쉬운 소프트웨어를 개발하기 위해 노력하고 있습니다.
-**Time2M** 중요
- 출시 기간 (TTM) 은 특히 교육 기술과 같은 경쟁이 치열한 시장에서 모든 소프트웨어 제품에 중요합니다.민첩한 개발 방법을 채택함으로써 우리는 우리의 소프트웨어를 신속하게 교체하고 개선할 수 있을 것이며, 우리로 하여금 경쟁사보다 더 빨리 제품을 시장에 내놓을 수 있게 할 것이다.이를 통해 시장 점유율을 확보하고 강력한 사용자 기반을 구축할 수 있습니다.
민첩성이란 무엇이며, 왜 그것이 매우 적합합니까?
> 민첩성은 반복 및 증분 개발, 팀워크 및 변화에 대한 적응성을 강조하는 소프트웨어 개발 방법입니다.다음과 같은 이유로 Calculus Visualizer 프로젝트에 적합합니다.
1.반복 및 증분 개발: 민첩성은 우리가 단계별로 소프트웨어를 구축하고 기본 기능부터 시작한 다음 사용자의 피드백에 따라 더 많은 기능과 개선을 추가할 수 있도록 허용한다.이를 통해 사용자에게 제품을 신속하게 전달하고 필요에 따라 개발 로드맵을 조정할 수 있습니다.
2. 팀워크: 민첩성은 팀워크와 다기능 협력을 강조한다.이것은 정확하고 사용자 친화적인 소프트웨어를 만들기 위해 수학자, 소프트웨어 엔지니어 및 사용자 경험 디자이너가 함께 노력해야 하기 때문에 프로젝트에 매우 중요합니다.
3. 변화에 대한 적응성: 민첩한 개발은 끊임없이 변화하는 수요와 우선순위에 적응할수 있다.사용자 피드백을 수집하고 요구 사항에 대한 자세한 내용을 파악할 때 가장 중요한 기능에 집중할 수 있도록 개발 로드맵을 유연하게 조정할 수 있습니다.그러므로 우리는 민첩성을 선택한다
> 결론적으로 민첩한 개발은 미적분 시각화 소프트웨어를 개발하는 가장 좋은 방법이다.이를 통해 우리는 빠르게 교체하고 변화에 적응하며 사용자와 협력하고 시장 점유율을 얻을 수 있습니다.우리는 민첩한 방법을 채택함으로써 학생과 교육자가 수학을 배우고 가르치는 방식을 완전히 바꿀 수 있는 창의적인 소프트웨어를 만들 수 있다고 믿는다.
# #
# # # 소프트웨어의 가능한 용도 (즉, 고등 수학을 준비하는 학생들을 위한 대상 시장)
- * * 교육 기관 (예: 학교, 대학교) * * 이 코드는 함수, 포인트 및 혁명 볼륨을 시각화하는 데 도움이 되는 교육 도구로 사용됩니다.또한 미적분 개념을 보다 상호 작용적이고 매력적인 방식으로 시연하는 데 사용될 수 있습니다.
- ** 미적분 과정 학생 및 교육자 **
- 시각적 미적분 개념에 관심 있는 개인
# #
# # # 개발 프로세스
- 민첩성: 스크럼 방법론
* * 구성 요소: * *
1. ** 요구 사항 수집 및 분석: **
- 기능 요구 사항:
- 수학 함수를 그립니다.
- 함수의 적분을 계산합니다.
- 지정된 축을 중심으로 회전된 볼륨을 계산합니다.
- 비기능 요구 사항:
- 사용자 친화적인 그래픽 인터페이스.
- 효율적이고 정확한 계산.
- 향후 기능을 위해 확장 가능
    
UML
- 용례도:
  
<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/4.png"/>

- 순서도:
<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/3.png"/>


2. ** 디자인: **
- 고급 아키텍처:
- 사용자 입력 및 시각화를 위한 GUI
- 계산에 사용되는 수학 엔진입니다.
- 함수와 적분 데이터의 데이터 저장.
- 모듈 및 구성 요소:
- 기능 드로잉 모듈.
- 포인트 계산 모듈.
- 볼륨 계산 모듈.
- GUI 모듈.
3. ** 구현: **
- 프로그래밍 언어 및 도구:
구렁이
- GUI용 Tkinter
-NumPy 는 숫자 계산에 사용됩니다.
- 인쇄용 Matplotlib.
- 기호 계산의 Sympy입니다.
- 인코딩 표준:
-PEP 8 스타일 가이드.
- 단일 모듈에 대한 셀 테스트.
4. ** 테스트: **
- 유닛 테스트: 개별 모듈의 기능을 검증합니다.
- 통합 테스트: 모듈이 올바르게 작동되도록 합니다.
- 시스템 테스트: 소프트웨어의 전반적인 기능과 성능을 평가합니다.
5.** 배포:**
- 패키지: 배포를 위해 실행 파일이나 설치 프로그램을 만듭니다.
- 설치: 소프트웨어를 설치하기 위한 명확한 지침을 제공합니다.
- 문서: 사용자 안내서 및 기술 문서.
6.** 유지 관리:**
- 오류 추적: 사용자가 보고한 오류를 모니터링하고 수정합니다.
- 업데이트 및 패치: 기능을 개선하고 문제를 해결하기 위해 업데이트를 게시합니다.
- 기술 지원: 문제가 있는 사용자를 지원합니다.
# #

# # # 구성원 (역할, 책임 및 부분)
** 작업 1**: 사용자 인터페이스 및 그래픽 디스플레이 만들기(Shay)
- 입력 필드, 버튼 및 그래픽 디스플레이를 작성합니다.
- 직관적인 사용자 환경과 함께 어플리케이션을 사용하기 쉽도록 합니다.
** 작업 2**: 함수 해석, 적분 계산 및 볼륨 계산 구현(Steven)
- 함수 해석, 적분 계산 및 볼륨 계산을 위한 알고리즘을 구현합니다.
- 응용 프로그램이 수학적으로 정확하고 다양한 기능을 처리할 수 있는지 확인합니다.
**작업 3**: 데이터 시각화 설계 및 구현, Youtube를 통한 프레젠테이션 비디오(James) 제작
- 함수, 적분 및 볼륨 결과의 시각적 표현을 설계하고 구현합니다.
- 그래픽이 명확하고 정보가 풍부하며 이해하기 쉽도록 합니다.
** 작업 4**: 테스트 및 문서(전체 3명)
- 애플리케이션의 기능과 정확성을 검증하기 위한 테스트 용례를 작성하고 실행합니다.
- 응용 프로그램의 기능과 사용 방법을 설명하는 사용자 설명서와 문서를 작성합니다.
# # # 타임라인:
- 1주차(3/11-3/18): 작업 시작 1 및 2
- 2주차(3/33/30): 작업 시작 3
- 3주차(4/5-4/12): 작업 완료 1, 2, 3
- 4주차(4/20년 4월 13일~4일): 임무 완료4
# # # # 커뮤니케이션 프로그램:
-** 일일 스탠딩 세션 **: 진행, 장애물 및 다음 단계를 논의하는 간단한 일일 세션입니다.
-** 코드 검토 **: 코드 검토는 품질 및 일관성을 보장하기 위해 코드를 커밋하기 전에 수행됩니다.
-** 인스턴트 메시징 **: Slack 또는 Microsoft Teams와 같은 인스턴트 메시징 플랫폼은 신속한 의사 소통과 문제 해결을 위해 사용됩니다.
# #
일정
1. Tkinter, matplotlib, numpy 및 sympy를 포함하여 필요한 모듈과 라이브러리를 가져옵니다.
2. plot_volume_around_aaxis라는 함수를 정의하여 지정된 축 주위의 볼륨을 계산하고 그립니다.
3. on_plot_hover라는 함수를 정의하여 마우스오버 이벤트를 처리하고 도면의 데이터 점 좌표를 표시합니다.
4. 함수와 적분을 그리고 계산된 볼륨을 표시하는 plot_function_integral_volume이라는 함수를 정의합니다.
6. 윈도우라는 Tkinter 창을 만들고 창 제목, 크기 및 스타일을 설정합니다.
7. 창에 기본 프레임 main_frame을 만들어 다른 GUI 요소를 포함합니다.
8. 기본 프레임에 레이블, 입력 필드, 확인란, 버튼 및 텍스트 레이블을 만들어 사용자 입력을 받아 결과를 표시합니다.
9. 기본 프레임의 행과 열의 가중치를 설정하여 창 크기가 변경될 때 레이아웃에 맞게 조정할 수 있도록 합니다.
10. Tkinter 이벤트 루프를 시작하여 사용자 상호 작용을 기다립니다.
# #
# # # 알고리즘 *
함수 및 적분 드로잉:
-Sympy 계산:
  
```
 x_symbol = sp.symbols('x')
original_function = sp.sympify(function_input)
integral_function = sp.integrate(original_function, x_symbol)
```
- Matplotlib 드로잉:
  
```
fig, axs = plt.subplots(3, 1, figsize=(8, 12), gridspec_kw={'height_ratios': [1, 1, 0.5], 'hspace': 0.5})
x_vals = np.linspace(start, end, 400)

# Plot original function
f_original_lambdified = sp.lambdify(x_symbol, original_function, 'numpy')
y_vals_original = f_original_lambdified(x_vals)
axs[0].plot(x_vals, y_vals_original, label=f'f(x)={original_function}')
axs[0].set_title('Original Function Plot')
axs[0].grid(True)
axs[0].legend()

# Plot integral function
f_integral_lambdified = sp.lambdify(x_symbol, integral_function, 'numpy')
y_vals_integral = f_integral_lambdified(x_vals)
axs[1].plot(x_vals, y_vals_integral, label=f'Integral of f(x)={integral_function}')
axs[1].set_title('Integral Plot(Withou C)')
axs[1].grid(True)
axs[1].legend()

# Display integral result
integral_result = integral_function.subs(x_symbol, end) - integral_function.subs(x_symbol, start)
axs[2].text(0.5, 0.5, f'Integral Result: {integral_result.evalf()}', horizontalalignment='center', verticalalignment='center', transform=axs[2].transAxes)
axs[2].axis('off')

```
볼륨 계산 및 드로잉:
-Sympy 계산:
  
```
if axis == 'x':
    volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))
else:  # y-axis
    volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))

```
- Matplotlib 드로잉:
```
if axis == 'x':
    volume = sp.pi * sp.integrate(function**2, (x_symbol, start, end))
else:  # y-axis
    volume = sp.pi * sp.integrate(function**2, (x_symbol, start, end))
    
integral_function = sp.integrate(function, x_symbol)
f_lambdified = sp.lambdify(x_symbol, integral_function, 'numpy')

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(start, end, 100)
phi = np.linspace(0, 2 * np.pi, 100)
X, P = np.meshgrid(x, phi)

R = f_lambdified(X)
if axis == 'x':
    Y = R * np.cos(P)
    Z = R * np.sin(P)
else:  # Around y-axis
    Y = X
    X = R * np.cos(P)
    Z = R * np.sin(P)

ax.plot_surface(X, Y, Z, color='b', alpha=0.6)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
# 
ax.set_title(f'Volume around {axis.upper()}-axis: {volume.evalf()}')

plt.show()

```
마우스 정지 이벤트:
- Matplotlib 이벤트 처리:
  
```
def on_plot_hover(event, axs, fig, canvas):
    for ax in axs:
        if event.inaxes == ax:
            for line in ax.get_lines():
                cont, ind = line.contains(event)
                if cont:
                    xdata, ydata = line.get_data()
                    x, y = xdata[ind["ind"][0]], ydata[ind["ind"][0]]
                    annot = ax.annotate(f"({x:.2f}, {y:.2f})", xy=(x, y), xytext=(20, 20), textcoords="offset points",
                                        bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
                                        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))
                    fig.canvas.draw_idle()
                    def remove_annot():
                        annot.remove()
                        fig.canvas.draw_idle()
                    fig.canvas.mpl_connect("motion_notify_event", lambda event: remove_annot())
```
추가 기능
- Tkinter 위젯:
  
```
window = tk.Tk()
window.title("Calculus Visualizer")
style = ttk.Style()
style.theme_use('clam')
window.minsize(600, 400)
main_frame = ttk.Frame(window, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

```
- 탐색 도구 모음 2Tk:
  
```
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas_widget.grid(row=5, column=0, columnspan=4)
canvas.mpl_connect('motion_notify_event', lambda event: on_plot_hover(event, axs, fig, canvas))

toolbar_frame = ttk.Frame(window) 
toolbar_frame.grid(row=4, column=0, columnspan=4, sticky=(tk.W, tk.E))  
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)  
toolbar.update()

```
# #
# # 소프트웨어의 현재 상태
-Alpha Release: 기능 및 전체 드로잉을 포함한 기본 기능을 구현합니다.
- 베타 버전 (예정): 볼륨 계산 및 시각화 기능이 추가됩니다.
- 안정적 게시 (예정): 사용자 인터페이스 개선 사항 및 버그 수정이 구현됩니다.
# #
# # # 향후 계획
- 고급 기능:
- 3D 공간에 커브 그리기
- 사용자 정의 함수 통합
- 교육 자료:
- 온라인 학습 플랫폼과의 통합
- 대화형 자습서 및 시뮬레이션 개발
공동 작업
- 지역 사회 공헌을 위한 오픈 소스 소프트웨어
- 교육자와 협력하여 교육적 가치 향상
공지
** 구체적으로 코드 조각은 다음과 같은 패키지를 사용합니다. **
  
- **Sympy**: 함수 해석, 적분 계산 및 볼륨 계산.
- **NumPy**: 데이터 점을 생성하고 메쉬를 만듭니다.
- **Matplotlib**: 3D 곡면 다이어그램, 원본 함수 다이어그램 및 적분 함수 다이어그램을 작성합니다.
- **Tkinter**: GUI 창, 버튼, 레이블 및 기타 위젯을 작성합니다.
  
> 은 (는) 이러한 외부 패키지를 활용하여 코드 조각을 처음부터 이러한 기능을 구현하지 않고도 함수와 적분을 계산하고 시각화하는 등 핵심 기능에 집중할 수 있습니다.
