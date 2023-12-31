上記の2つのシングルトンパターンの実装を解説します。1つ目の実装はクラスをベースにしたシングルトンパターンであり、2つ目の実装はメタクラスを使用したシングルトンパターンです。

## 1つ目の実装 - クラスベースのシングルトンパターン

```python
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Myclass(Singleton):
    def __init__(self, input):
        self.input = input
```

この実装では、`Singleton` クラスがシングルトンの振る舞いを提供します。`__new__`
メソッドをオーバーライドして、クラスが初めてインスタンス化されたときにインスタンスを生成し、それ以降は既存のインスタンスを返します。
これにより、同じクラスから作成されたすべてのインスタンスが同じオブジェクトを共有します。

## 2つ目の実装 - メタクラスを使用したシングルトンパターン

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        # シングルトンのインスタンスに対するビジネスロジックを定義します
        # ...
```

この実装では、`SingletonMeta`
というメタクラスを定義し、シングルトンの機能を提供します。`__call__`
メソッドをオーバーライドして、クラスが初めてインスタンス化されたときにインスタンスを生成し、それ以降は既存のインスタンスを返します。
メタクラスの`__call__`
メソッドは、クラスを関数のように呼び出すときに実行されます。

`Singleton` クラスは `SingletonMeta`
メタクラスを使用して定義され、シングルトンの機能を持つクラスとして機能します。`some_business_logic`
メソッドは、シングルトンのインスタンスに対するビジネスロジックを定義するための例です。

これらの実装のいずれも、同じクラスから作成されたインスタンスが常に同じオブジェクトを共有し、シングルトンの振る舞いを提供します。
選択肢はどちらも優れた方法であり、プロジェクトの要件に合わせて選択できます。

## 備忘録

(1) __new__と__init__とは、何が違うのか？

1. **new__の場合　(以下、"Python言語リファレンス"より引用)
   クラスclsの新しいインスタンスを作るために呼び出されます。
   インスタンスを生成するよう要求されているクラスclsを第一引数にとります。
   残りの引数はオブジェクトのコンストラクタの式 (クラスの呼び出し文)
   に渡されます。 **new**()の戻り値は、新しいオブジェクトのインスタンス (通常は
   cls のインスタンス) でなければなりません。
   典型的な実装では、クラスの新たなインスタンスを生成するときには
   super().**new**(cls[,
   ...])に適切な引数を指定してスーパクラスの__new**()メソッドを呼び出し、新たに生成されたインスタンスに必要な変更を加えてから返します。
   **new**()が、clsのインスタンスを返さない場合、インスタンスの__init__()メソッドは呼び出されません。
   **new**()の主な目的は、変更不能な型 (int, str, tuple など)
   のサブクラスでインスタンス生成をカスタマイズすることにあります。また、クラス生成をカスタマイズするために、カスタムのメタクラスでよくオーバーライドされます。
   インスタンスオブジェクトが生成される前に呼ばれ、第一引数clsには、クラスオブジェクトが代入されていて、オブジェクトselfをインスタンス化することを目的とするんですね。

※python2.7系と、python3系では、__new__メソッドへの引数の与え方に差異が存在するため、注意が必要です。Web記事："How
To Use Python new Method Example"

2. **init__の場合　(以下、"Python言語リファレンス"より引用) インスタンスが
   (**new**()によって)
   生成された後、それが呼び出し元に返される前に呼び出されます。
   引数はクラスのコンストラクタ式に渡したものです。
   基底クラスとその派生クラスがともに__init**()メソッドを持つ場合、派生クラスの__init__()メソッドは基底クラスの
   **init**()メソッドを明示的に呼び出して、インスタンスの基底クラス部分が適切に初期化されること保証しなければなりません。例えば、super().**init**([args...])
   。
   **new**()と__init__()は連携してオブジェクトを構成する(**new**()が作成し、**init**()がそれをカスタマイズする)ので、**init**()から非None値を返してはいけません;
   そうしてしまうと、実行時に TypeError が送出されてしまいます。
   インスタンスオブジェクトが生成された後に呼ばれ、第一引数selfには、インスタンスオブジェクトが代入されていて、オブジェクトselfを初期化することを目的とするんですね。
