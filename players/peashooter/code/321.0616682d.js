(self["webpackChunkfake_qq_chat_window"] = self["webpackChunkfake_qq_chat_window"] || []).push([[321], {
    3037: function(e, t, r) {
        var n = r(9969)
          , o = TypeError;
        e.exports = function(e, t) {
            if (n(t, e))
                return e;
            throw o("Incorrect invocation")
        }
    },
    6525: function(e) {
        e.exports = "undefined" != typeof ArrayBuffer && "undefined" != typeof DataView
    },
    7041: function(e, t, r) {
        "use strict";
        var n, o, s, i = r(6525), a = r(6454), c = r(4356), u = r(7385), l = r(8780), f = r(1829), d = r(947), p = r(1308), h = r(1347), m = r(1547), g = r(2262).f, y = r(9969), E = r(7001), w = r(1208), b = r(9002), R = r(5809), v = r(6228), A = v.enforce, _ = v.get, O = c.Int8Array, S = O && O.prototype, T = c.Uint8ClampedArray, C = T && T.prototype, N = O && E(O), x = S && E(S), k = Object.prototype, D = c.TypeError, j = b("toStringTag"), P = R("TYPED_ARRAY_TAG"), U = "TypedArrayConstructor", q = i && !!w && "Opera" !== d(c.opera), L = !1, I = {
            Int8Array: 1,
            Uint8Array: 1,
            Uint8ClampedArray: 1,
            Int16Array: 2,
            Uint16Array: 2,
            Int32Array: 4,
            Uint32Array: 4,
            Float32Array: 4,
            Float64Array: 8
        }, F = {
            BigInt64Array: 8,
            BigUint64Array: 8
        }, B = function(e) {
            if (!l(e))
                return !1;
            var t = d(e);
            return "DataView" === t || f(I, t) || f(F, t)
        }, M = function(e) {
            var t = E(e);
            if (l(t)) {
                var r = _(t);
                return r && f(r, U) ? r[U] : M(t)
            }
        }, H = function(e) {
            if (!l(e))
                return !1;
            var t = d(e);
            return f(I, t) || f(F, t)
        }, z = function(e) {
            if (H(e))
                return e;
            throw D("Target is not a typed array")
        }, W = function(e) {
            if (u(e) && (!w || y(N, e)))
                return e;
            throw D(p(e) + " is not a typed array constructor")
        }, V = function(e, t, r, n) {
            if (a) {
                if (r)
                    for (var o in I) {
                        var s = c[o];
                        if (s && f(s.prototype, e))
                            try {
                                delete s.prototype[e]
                            } catch (i) {
                                try {
                                    s.prototype[e] = t
                                } catch (u) {}
                            }
                    }
                x[e] && !r || m(x, e, r ? t : q && S[e] || t, n)
            }
        }, J = function(e, t, r) {
            var n, o;
            if (a) {
                if (w) {
                    if (r)
                        for (n in I)
                            if (o = c[n],
                            o && f(o, e))
                                try {
                                    delete o[e]
                                } catch (s) {}
                    if (N[e] && !r)
                        return;
                    try {
                        return m(N, e, r ? t : q && N[e] || t)
                    } catch (s) {}
                }
                for (n in I)
                    o = c[n],
                    !o || o[e] && !r || m(o, e, t)
            }
        };
        for (n in I)
            o = c[n],
            s = o && o.prototype,
            s ? A(s)[U] = o : q = !1;
        for (n in F)
            o = c[n],
            s = o && o.prototype,
            s && (A(s)[U] = o);
        if ((!q || !u(N) || N === Function.prototype) && (N = function() {
            throw D("Incorrect invocation")
        }
        ,
        q))
            for (n in I)
                c[n] && w(c[n], N);
        if ((!q || !x || x === k) && (x = N.prototype,
        q))
            for (n in I)
                c[n] && w(c[n].prototype, x);
        if (q && E(C) !== x && w(C, x),
        a && !f(x, j))
            for (n in L = !0,
            g(x, j, {
                get: function() {
                    return l(this) ? this[P] : void 0
                }
            }),
            I)
                c[n] && h(c[n], P, n);
        e.exports = {
            NATIVE_ARRAY_BUFFER_VIEWS: q,
            TYPED_ARRAY_TAG: L && P,
            aTypedArray: z,
            aTypedArrayConstructor: W,
            exportTypedArrayMethod: V,
            exportTypedArrayStaticMethod: J,
            getTypedArrayConstructor: M,
            isView: B,
            isTypedArray: H,
            TypedArray: N,
            TypedArrayPrototype: x
        }
    },
    9171: function(e, t, r) {
        var n = r(7629)
          , o = r(8043)
          , s = r(7465)
          , i = r(7687)
          , a = function(e) {
            var t = 1 == e;
            return function(r, a, c) {
                var u, l, f = s(r), d = o(f), p = n(a, c), h = i(d);
                while (h-- > 0)
                    if (u = d[h],
                    l = p(u, h, f),
                    l)
                        switch (e) {
                        case 0:
                            return u;
                        case 1:
                            return h
                        }
                return t ? -1 : void 0
            }
        };
        e.exports = {
            findLast: a(0),
            findLastIndex: a(1)
        }
    },
    4952: function(e, t, r) {
        var n = r(7991);
        e.exports = !n((function() {
            function e() {}
            return e.prototype.constructor = null,
            Object.getPrototypeOf(new e) !== e.prototype
        }
        ))
    },
    7791: function(e) {
        e.exports = {
            IndexSizeError: {
                s: "INDEX_SIZE_ERR",
                c: 1,
                m: 1
            },
            DOMStringSizeError: {
                s: "DOMSTRING_SIZE_ERR",
                c: 2,
                m: 0
            },
            HierarchyRequestError: {
                s: "HIERARCHY_REQUEST_ERR",
                c: 3,
                m: 1
            },
            WrongDocumentError: {
                s: "WRONG_DOCUMENT_ERR",
                c: 4,
                m: 1
            },
            InvalidCharacterError: {
                s: "INVALID_CHARACTER_ERR",
                c: 5,
                m: 1
            },
            NoDataAllowedError: {
                s: "NO_DATA_ALLOWED_ERR",
                c: 6,
                m: 0
            },
            NoModificationAllowedError: {
                s: "NO_MODIFICATION_ALLOWED_ERR",
                c: 7,
                m: 1
            },
            NotFoundError: {
                s: "NOT_FOUND_ERR",
                c: 8,
                m: 1
            },
            NotSupportedError: {
                s: "NOT_SUPPORTED_ERR",
                c: 9,
                m: 1
            },
            InUseAttributeError: {
                s: "INUSE_ATTRIBUTE_ERR",
                c: 10,
                m: 1
            },
            InvalidStateError: {
                s: "INVALID_STATE_ERR",
                c: 11,
                m: 1
            },
            SyntaxError: {
                s: "SYNTAX_ERR",
                c: 12,
                m: 1
            },
            InvalidModificationError: {
                s: "INVALID_MODIFICATION_ERR",
                c: 13,
                m: 1
            },
            NamespaceError: {
                s: "NAMESPACE_ERR",
                c: 14,
                m: 1
            },
            InvalidAccessError: {
                s: "INVALID_ACCESS_ERR",
                c: 15,
                m: 1
            },
            ValidationError: {
                s: "VALIDATION_ERR",
                c: 16,
                m: 0
            },
            TypeMismatchError: {
                s: "TYPE_MISMATCH_ERR",
                c: 17,
                m: 1
            },
            SecurityError: {
                s: "SECURITY_ERR",
                c: 18,
                m: 1
            },
            NetworkError: {
                s: "NETWORK_ERR",
                c: 19,
                m: 1
            },
            AbortError: {
                s: "ABORT_ERR",
                c: 20,
                m: 1
            },
            URLMismatchError: {
                s: "URL_MISMATCH_ERR",
                c: 21,
                m: 1
            },
            QuotaExceededError: {
                s: "QUOTA_EXCEEDED_ERR",
                c: 22,
                m: 1
            },
            TimeoutError: {
                s: "TIMEOUT_ERR",
                c: 23,
                m: 1
            },
            InvalidNodeTypeError: {
                s: "INVALID_NODE_TYPE_ERR",
                c: 24,
                m: 1
            },
            DataCloneError: {
                s: "DATA_CLONE_ERR",
                c: 25,
                m: 1
            }
        }
    },
    7629: function(e, t, r) {
        var n = r(1203)
          , o = r(5438)
          , s = r(7943)
          , i = n(n.bind);
        e.exports = function(e, t) {
            return o(e),
            void 0 === t ? e : s ? i(e, t) : function() {
                return e.apply(t, arguments)
            }
        }
    },
    7001: function(e, t, r) {
        var n = r(1829)
          , o = r(7385)
          , s = r(7465)
          , i = r(6951)
          , a = r(4952)
          , c = i("IE_PROTO")
          , u = Object
          , l = u.prototype;
        e.exports = a ? u.getPrototypeOf : function(e) {
            var t = s(e);
            if (n(t, c))
                return t[c];
            var r = t.constructor;
            return o(r) && t instanceof r ? r.prototype : t instanceof u ? l : null
        }
    },
    1913: function(e, t, r) {
        "use strict";
        var n = r(7041)
          , o = r(7687)
          , s = r(218)
          , i = n.aTypedArray
          , a = n.exportTypedArrayMethod;
        a("at", (function(e) {
            var t = i(this)
              , r = o(t)
              , n = s(e)
              , a = n >= 0 ? n : r + n;
            return a < 0 || a >= r ? void 0 : t[a]
        }
        ))
    },
    3284: function(e, t, r) {
        "use strict";
        var n = r(7041)
          , o = r(9171).findLastIndex
          , s = n.aTypedArray
          , i = n.exportTypedArrayMethod;
        i("findLastIndex", (function(e) {
            return o(s(this), e, arguments.length > 1 ? arguments[1] : void 0)
        }
        ))
    },
    2834: function(e, t, r) {
        "use strict";
        var n = r(7041)
          , o = r(9171).findLast
          , s = n.aTypedArray
          , i = n.exportTypedArrayMethod;
        i("findLast", (function(e) {
            return o(s(this), e, arguments.length > 1 ? arguments[1] : void 0)
        }
        ))
    },
    8498: function(e, t, r) {
        "use strict";
        var n = r(6602)
          , o = r(4356)
          , s = r(3867)
          , i = r(9336)
          , a = r(2262).f
          , c = r(1829)
          , u = r(3037)
          , l = r(3385)
          , f = r(1389)
          , d = r(7791)
          , p = r(2968)
          , h = r(6454)
          , m = r(7148)
          , g = "DOMException"
          , y = s("Error")
          , E = s(g)
          , w = function() {
            u(this, b);
            var e = arguments.length
              , t = f(e < 1 ? void 0 : arguments[0])
              , r = f(e < 2 ? void 0 : arguments[1], "Error")
              , n = new E(t,r)
              , o = y(t);
            return o.name = g,
            a(n, "stack", i(1, p(o.stack, 1))),
            l(n, this, w),
            n
        }
          , b = w.prototype = E.prototype
          , R = "stack"in y(g)
          , v = "stack"in new E(1,2)
          , A = E && h && Object.getOwnPropertyDescriptor(o, g)
          , _ = !!A && !(A.writable && A.configurable)
          , O = R && !_ && !v;
        n({
            global: !0,
            constructor: !0,
            forced: m || O
        }, {
            DOMException: O ? w : E
        });
        var S = s(g)
          , T = S.prototype;
        if (T.constructor !== S)
            for (var C in m || a(T, "constructor", i(1, S)),
            d)
                if (c(d, C)) {
                    var N = d[C]
                      , x = N.s;
                    c(S, x) || a(S, x, i(6, N.c))
                }
    },
    5321: function(e, t, r) {
        "use strict";
        r.r(t),
        r.d(t, {
            default: function() {
                return Sr
            }
        });
        r(7200);
        var n = r(3990);
        r(1913),
        r(2834),
        r(3284),
        r(9751);
        function o(e, t) {
            return function() {
                return e.apply(t, arguments)
            }
        }
        const {toString: s} = Object.prototype
          , {getPrototypeOf: i} = Object
          , a = (e=>t=>{
            const r = s.call(t);
            return e[r] || (e[r] = r.slice(8, -1).toLowerCase())
        }
        )(Object.create(null))
          , c = e=>(e = e.toLowerCase(),
        t=>a(t) === e)
          , u = e=>t=>typeof t === e
          , {isArray: l} = Array
          , f = u("undefined");
        function d(e) {
            return null !== e && !f(e) && null !== e.constructor && !f(e.constructor) && g(e.constructor.isBuffer) && e.constructor.isBuffer(e)
        }
        const p = c("ArrayBuffer");
        function h(e) {
            let t;
            return t = "undefined" !== typeof ArrayBuffer && ArrayBuffer.isView ? ArrayBuffer.isView(e) : e && e.buffer && p(e.buffer),
            t
        }
        const m = u("string")
          , g = u("function")
          , y = u("number")
          , E = e=>null !== e && "object" === typeof e
          , w = e=>!0 === e || !1 === e
          , b = e=>{
            if ("object" !== a(e))
                return !1;
            const t = i(e);
            return (null === t || t === Object.prototype || null === Object.getPrototypeOf(t)) && !(Symbol.toStringTag in e) && !(Symbol.iterator in e)
        }
          , R = c("Date")
          , v = c("File")
          , A = c("Blob")
          , _ = c("FileList")
          , O = e=>E(e) && g(e.pipe)
          , S = e=>{
            let t;
            return e && ("function" === typeof FormData && e instanceof FormData || g(e.append) && ("formdata" === (t = a(e)) || "object" === t && g(e.toString) && "[object FormData]" === e.toString()))
        }
          , T = c("URLSearchParams")
          , C = e=>e.trim ? e.trim() : e.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, "");
        function N(e, t, {allOwnKeys: r=!1}={}) {
            if (null === e || "undefined" === typeof e)
                return;
            let n, o;
            if ("object" !== typeof e && (e = [e]),
            l(e))
                for (n = 0,
                o = e.length; n < o; n++)
                    t.call(null, e[n], n, e);
            else {
                const o = r ? Object.getOwnPropertyNames(e) : Object.keys(e)
                  , s = o.length;
                let i;
                for (n = 0; n < s; n++)
                    i = o[n],
                    t.call(null, e[i], i, e)
            }
        }
        function x(e, t) {
            t = t.toLowerCase();
            const r = Object.keys(e);
            let n, o = r.length;
            while (o-- > 0)
                if (n = r[o],
                t === n.toLowerCase())
                    return n;
            return null
        }
        const k = (()=>"undefined" !== typeof globalThis ? globalThis : "undefined" !== typeof self ? self : "undefined" !== typeof window ? window : global)()
          , D = e=>!f(e) && e !== k;
        function j() {
            const {caseless: e} = D(this) && this || {}
              , t = {}
              , r = (r,n)=>{
                const o = e && x(t, n) || n;
                b(t[o]) && b(r) ? t[o] = j(t[o], r) : b(r) ? t[o] = j({}, r) : l(r) ? t[o] = r.slice() : t[o] = r
            }
            ;
            for (let n = 0, o = arguments.length; n < o; n++)
                arguments[n] && N(arguments[n], r);
            return t
        }
        const P = (e,t,r,{allOwnKeys: n}={})=>(N(t, ((t,n)=>{
            r && g(t) ? e[n] = o(t, r) : e[n] = t
        }
        ), {
            allOwnKeys: n
        }),
        e)
          , U = e=>(65279 === e.charCodeAt(0) && (e = e.slice(1)),
        e)
          , q = (e,t,r,n)=>{
            e.prototype = Object.create(t.prototype, n),
            e.prototype.constructor = e,
            Object.defineProperty(e, "super", {
                value: t.prototype
            }),
            r && Object.assign(e.prototype, r)
        }
          , L = (e,t,r,n)=>{
            let o, s, a;
            const c = {};
            if (t = t || {},
            null == e)
                return t;
            do {
                o = Object.getOwnPropertyNames(e),
                s = o.length;
                while (s-- > 0)
                    a = o[s],
                    n && !n(a, e, t) || c[a] || (t[a] = e[a],
                    c[a] = !0);
                e = !1 !== r && i(e)
            } while (e && (!r || r(e, t)) && e !== Object.prototype);
            return t
        }
          , I = (e,t,r)=>{
            e = String(e),
            (void 0 === r || r > e.length) && (r = e.length),
            r -= t.length;
            const n = e.indexOf(t, r);
            return -1 !== n && n === r
        }
          , F = e=>{
            if (!e)
                return null;
            if (l(e))
                return e;
            let t = e.length;
            if (!y(t))
                return null;
            const r = new Array(t);
            while (t-- > 0)
                r[t] = e[t];
            return r
        }
          , B = (e=>t=>e && t instanceof e)("undefined" !== typeof Uint8Array && i(Uint8Array))
          , M = (e,t)=>{
            const r = e && e[Symbol.iterator]
              , n = r.call(e);
            let o;
            while ((o = n.next()) && !o.done) {
                const r = o.value;
                t.call(e, r[0], r[1])
            }
        }
          , H = (e,t)=>{
            let r;
            const n = [];
            while (null !== (r = e.exec(t)))
                n.push(r);
            return n
        }
          , z = c("HTMLFormElement")
          , W = e=>e.toLowerCase().replace(/[-_\s]([a-z\d])(\w*)/g, (function(e, t, r) {
            return t.toUpperCase() + r
        }
        ))
          , V = (({hasOwnProperty: e})=>(t,r)=>e.call(t, r))(Object.prototype)
          , J = c("RegExp")
          , K = (e,t)=>{
            const r = Object.getOwnPropertyDescriptors(e)
              , n = {};
            N(r, ((r,o)=>{
                let s;
                !1 !== (s = t(r, o, e)) && (n[o] = s || r)
            }
            )),
            Object.defineProperties(e, n)
        }
          , $ = e=>{
            K(e, ((t,r)=>{
                if (g(e) && -1 !== ["arguments", "caller", "callee"].indexOf(r))
                    return !1;
                const n = e[r];
                g(n) && (t.enumerable = !1,
                "writable"in t ? t.writable = !1 : t.set || (t.set = ()=>{
                    throw Error("Can not rewrite read-only method '" + r + "'")
                }
                ))
            }
            ))
        }
          , G = (e,t)=>{
            const r = {}
              , n = e=>{
                e.forEach((e=>{
                    r[e] = !0
                }
                ))
            }
            ;
            return l(e) ? n(e) : n(String(e).split(t)),
            r
        }
          , Y = ()=>{}
          , Z = (e,t)=>(e = +e,
        Number.isFinite(e) ? e : t)
          , Q = "abcdefghijklmnopqrstuvwxyz"
          , X = "0123456789"
          , ee = {
            DIGIT: X,
            ALPHA: Q,
            ALPHA_DIGIT: Q + Q.toUpperCase() + X
        }
          , te = (e=16,t=ee.ALPHA_DIGIT)=>{
            let r = "";
            const {length: n} = t;
            while (e--)
                r += t[Math.random() * n | 0];
            return r
        }
        ;
        function re(e) {
            return !!(e && g(e.append) && "FormData" === e[Symbol.toStringTag] && e[Symbol.iterator])
        }
        const ne = e=>{
            const t = new Array(10)
              , r = (e,n)=>{
                if (E(e)) {
                    if (t.indexOf(e) >= 0)
                        return;
                    if (!("toJSON"in e)) {
                        t[n] = e;
                        const o = l(e) ? [] : {};
                        return N(e, ((e,t)=>{
                            const s = r(e, n + 1);
                            !f(s) && (o[t] = s)
                        }
                        )),
                        t[n] = void 0,
                        o
                    }
                }
                return e
            }
            ;
            return r(e, 0)
        }
          , oe = c("AsyncFunction")
          , se = e=>e && (E(e) || g(e)) && g(e.then) && g(e.catch);
        var ie = {
            isArray: l,
            isArrayBuffer: p,
            isBuffer: d,
            isFormData: S,
            isArrayBufferView: h,
            isString: m,
            isNumber: y,
            isBoolean: w,
            isObject: E,
            isPlainObject: b,
            isUndefined: f,
            isDate: R,
            isFile: v,
            isBlob: A,
            isRegExp: J,
            isFunction: g,
            isStream: O,
            isURLSearchParams: T,
            isTypedArray: B,
            isFileList: _,
            forEach: N,
            merge: j,
            extend: P,
            trim: C,
            stripBOM: U,
            inherits: q,
            toFlatObject: L,
            kindOf: a,
            kindOfTest: c,
            endsWith: I,
            toArray: F,
            forEachEntry: M,
            matchAll: H,
            isHTMLForm: z,
            hasOwnProperty: V,
            hasOwnProp: V,
            reduceDescriptors: K,
            freezeMethods: $,
            toObjectSet: G,
            toCamelCase: W,
            noop: Y,
            toFiniteNumber: Z,
            findKey: x,
            global: k,
            isContextDefined: D,
            ALPHABET: ee,
            generateString: te,
            isSpecCompliantForm: re,
            toJSONObject: ne,
            isAsyncFn: oe,
            isThenable: se
        };
        r(1325);
        function ae(e, t, r, n, o) {
            Error.call(this),
            Error.captureStackTrace ? Error.captureStackTrace(this, this.constructor) : this.stack = (new Error).stack,
            this.message = e,
            this.name = "AxiosError",
            t && (this.code = t),
            r && (this.config = r),
            n && (this.request = n),
            o && (this.response = o)
        }
        ie.inherits(ae, Error, {
            toJSON: function() {
                return {
                    message: this.message,
                    name: this.name,
                    description: this.description,
                    number: this.number,
                    fileName: this.fileName,
                    lineNumber: this.lineNumber,
                    columnNumber: this.columnNumber,
                    stack: this.stack,
                    config: ie.toJSONObject(this.config),
                    code: this.code,
                    status: this.response && this.response.status ? this.response.status : null
                }
            }
        });
        const ce = ae.prototype
          , ue = {};
        ["ERR_BAD_OPTION_VALUE", "ERR_BAD_OPTION", "ECONNABORTED", "ETIMEDOUT", "ERR_NETWORK", "ERR_FR_TOO_MANY_REDIRECTS", "ERR_DEPRECATED", "ERR_BAD_RESPONSE", "ERR_BAD_REQUEST", "ERR_CANCELED", "ERR_NOT_SUPPORT", "ERR_INVALID_URL"].forEach((e=>{
            ue[e] = {
                value: e
            }
        }
        )),
        Object.defineProperties(ae, ue),
        Object.defineProperty(ce, "isAxiosError", {
            value: !0
        }),
        ae.from = (e,t,r,n,o,s)=>{
            const i = Object.create(ce);
            return ie.toFlatObject(e, i, (function(e) {
                return e !== Error.prototype
            }
            ), (e=>"isAxiosError" !== e)),
            ae.call(i, e.message, t, r, n, o),
            i.cause = e,
            i.name = e.name,
            s && Object.assign(i, s),
            i
        }
        ;
        var le = ae
          , fe = null;
        function de(e) {
            return ie.isPlainObject(e) || ie.isArray(e)
        }
        function pe(e) {
            return ie.endsWith(e, "[]") ? e.slice(0, -2) : e
        }
        function he(e, t, r) {
            return e ? e.concat(t).map((function(e, t) {
                return e = pe(e),
                !r && t ? "[" + e + "]" : e
            }
            )).join(r ? "." : "") : t
        }
        function me(e) {
            return ie.isArray(e) && !e.some(de)
        }
        const ge = ie.toFlatObject(ie, {}, null, (function(e) {
            return /^is[A-Z]/.test(e)
        }
        ));
        function ye(e, t, r) {
            if (!ie.isObject(e))
                throw new TypeError("target must be an object");
            t = t || new (fe || FormData),
            r = ie.toFlatObject(r, {
                metaTokens: !0,
                dots: !1,
                indexes: !1
            }, !1, (function(e, t) {
                return !ie.isUndefined(t[e])
            }
            ));
            const n = r.metaTokens
              , o = r.visitor || l
              , s = r.dots
              , i = r.indexes
              , a = r.Blob || "undefined" !== typeof Blob && Blob
              , c = a && ie.isSpecCompliantForm(t);
            if (!ie.isFunction(o))
                throw new TypeError("visitor must be a function");
            function u(e) {
                if (null === e)
                    return "";
                if (ie.isDate(e))
                    return e.toISOString();
                if (!c && ie.isBlob(e))
                    throw new le("Blob is not supported. Use a Buffer instead.");
                return ie.isArrayBuffer(e) || ie.isTypedArray(e) ? c && "function" === typeof Blob ? new Blob([e]) : Buffer.from(e) : e
            }
            function l(e, r, o) {
                let a = e;
                if (e && !o && "object" === typeof e)
                    if (ie.endsWith(r, "{}"))
                        r = n ? r : r.slice(0, -2),
                        e = JSON.stringify(e);
                    else if (ie.isArray(e) && me(e) || (ie.isFileList(e) || ie.endsWith(r, "[]")) && (a = ie.toArray(e)))
                        return r = pe(r),
                        a.forEach((function(e, n) {
                            !ie.isUndefined(e) && null !== e && t.append(!0 === i ? he([r], n, s) : null === i ? r : r + "[]", u(e))
                        }
                        )),
                        !1;
                return !!de(e) || (t.append(he(o, r, s), u(e)),
                !1)
            }
            const f = []
              , d = Object.assign(ge, {
                defaultVisitor: l,
                convertValue: u,
                isVisitable: de
            });
            function p(e, r) {
                if (!ie.isUndefined(e)) {
                    if (-1 !== f.indexOf(e))
                        throw Error("Circular reference detected in " + r.join("."));
                    f.push(e),
                    ie.forEach(e, (function(e, n) {
                        const s = !(ie.isUndefined(e) || null === e) && o.call(t, e, ie.isString(n) ? n.trim() : n, r, d);
                        !0 === s && p(e, r ? r.concat(n) : [n])
                    }
                    )),
                    f.pop()
                }
            }
            if (!ie.isObject(e))
                throw new TypeError("data must be an object");
            return p(e),
            t
        }
        var Ee = ye;
        function we(e) {
            const t = {
                "!": "%21",
                "'": "%27",
                "(": "%28",
                ")": "%29",
                "~": "%7E",
                "%20": "+",
                "%00": "\0"
            };
            return encodeURIComponent(e).replace(/[!'()~]|%20|%00/g, (function(e) {
                return t[e]
            }
            ))
        }
        function be(e, t) {
            this._pairs = [],
            e && Ee(e, this, t)
        }
        const Re = be.prototype;
        Re.append = function(e, t) {
            this._pairs.push([e, t])
        }
        ,
        Re.toString = function(e) {
            const t = e ? function(t) {
                return e.call(this, t, we)
            }
            : we;
            return this._pairs.map((function(e) {
                return t(e[0]) + "=" + t(e[1])
            }
            ), "").join("&")
        }
        ;
        var ve = be;
        function Ae(e) {
            return encodeURIComponent(e).replace(/%3A/gi, ":").replace(/%24/g, "$").replace(/%2C/gi, ",").replace(/%20/g, "+").replace(/%5B/gi, "[").replace(/%5D/gi, "]")
        }
        function _e(e, t, r) {
            if (!t)
                return e;
            const n = r && r.encode || Ae
              , o = r && r.serialize;
            let s;
            if (s = o ? o(t, r) : ie.isURLSearchParams(t) ? t.toString() : new ve(t,r).toString(n),
            s) {
                const t = e.indexOf("#");
                -1 !== t && (e = e.slice(0, t)),
                e += (-1 === e.indexOf("?") ? "?" : "&") + s
            }
            return e
        }
        class Oe {
            constructor() {
                this.handlers = []
            }
            use(e, t, r) {
                return this.handlers.push({
                    fulfilled: e,
                    rejected: t,
                    synchronous: !!r && r.synchronous,
                    runWhen: r ? r.runWhen : null
                }),
                this.handlers.length - 1
            }
            eject(e) {
                this.handlers[e] && (this.handlers[e] = null)
            }
            clear() {
                this.handlers && (this.handlers = [])
            }
            forEach(e) {
                ie.forEach(this.handlers, (function(t) {
                    null !== t && e(t)
                }
                ))
            }
        }
        var Se = Oe
          , Te = {
            silentJSONParsing: !0,
            forcedJSONParsing: !0,
            clarifyTimeoutError: !1
        }
          , Ce = "undefined" !== typeof URLSearchParams ? URLSearchParams : ve
          , Ne = "undefined" !== typeof FormData ? FormData : null
          , xe = "undefined" !== typeof Blob ? Blob : null;
        const ke = (()=>{
            let e;
            return ("undefined" === typeof navigator || "ReactNative" !== (e = navigator.product) && "NativeScript" !== e && "NS" !== e) && ("undefined" !== typeof window && "undefined" !== typeof document)
        }
        )()
          , De = (()=>"undefined" !== typeof WorkerGlobalScope && self instanceof WorkerGlobalScope && "function" === typeof self.importScripts)();
        var je = {
            isBrowser: !0,
            classes: {
                URLSearchParams: Ce,
                FormData: Ne,
                Blob: xe
            },
            isStandardBrowserEnv: ke,
            isStandardBrowserWebWorkerEnv: De,
            protocols: ["http", "https", "file", "blob", "url", "data"]
        };
        function Pe(e, t) {
            return Ee(e, new je.classes.URLSearchParams, Object.assign({
                visitor: function(e, t, r, n) {
                    return je.isNode && ie.isBuffer(e) ? (this.append(t, e.toString("base64")),
                    !1) : n.defaultVisitor.apply(this, arguments)
                }
            }, t))
        }
        function Ue(e) {
            return ie.matchAll(/\w+|\[(\w*)]/g, e).map((e=>"[]" === e[0] ? "" : e[1] || e[0]))
        }
        function qe(e) {
            const t = {}
              , r = Object.keys(e);
            let n;
            const o = r.length;
            let s;
            for (n = 0; n < o; n++)
                s = r[n],
                t[s] = e[s];
            return t
        }
        function Le(e) {
            function t(e, r, n, o) {
                let s = e[o++];
                const i = Number.isFinite(+s)
                  , a = o >= e.length;
                if (s = !s && ie.isArray(n) ? n.length : s,
                a)
                    return ie.hasOwnProp(n, s) ? n[s] = [n[s], r] : n[s] = r,
                    !i;
                n[s] && ie.isObject(n[s]) || (n[s] = []);
                const c = t(e, r, n[s], o);
                return c && ie.isArray(n[s]) && (n[s] = qe(n[s])),
                !i
            }
            if (ie.isFormData(e) && ie.isFunction(e.entries)) {
                const r = {};
                return ie.forEachEntry(e, ((e,n)=>{
                    t(Ue(e), n, r, 0)
                }
                )),
                r
            }
            return null
        }
        var Ie = Le;
        function Fe(e, t, r) {
            if (ie.isString(e))
                try {
                    return (t || JSON.parse)(e),
                    ie.trim(e)
                } catch (n) {
                    if ("SyntaxError" !== n.name)
                        throw n
                }
            return (r || JSON.stringify)(e)
        }
        const Be = {
            transitional: Te,
            adapter: ["xhr", "http"],
            transformRequest: [function(e, t) {
                const r = t.getContentType() || ""
                  , n = r.indexOf("application/json") > -1
                  , o = ie.isObject(e);
                o && ie.isHTMLForm(e) && (e = new FormData(e));
                const s = ie.isFormData(e);
                if (s)
                    return n && n ? JSON.stringify(Ie(e)) : e;
                if (ie.isArrayBuffer(e) || ie.isBuffer(e) || ie.isStream(e) || ie.isFile(e) || ie.isBlob(e))
                    return e;
                if (ie.isArrayBufferView(e))
                    return e.buffer;
                if (ie.isURLSearchParams(e))
                    return t.setContentType("application/x-www-form-urlencoded;charset=utf-8", !1),
                    e.toString();
                let i;
                if (o) {
                    if (r.indexOf("application/x-www-form-urlencoded") > -1)
                        return Pe(e, this.formSerializer).toString();
                    if ((i = ie.isFileList(e)) || r.indexOf("multipart/form-data") > -1) {
                        const t = this.env && this.env.FormData;
                        return Ee(i ? {
                            "files[]": e
                        } : e, t && new t, this.formSerializer)
                    }
                }
                return o || n ? (t.setContentType("application/json", !1),
                Fe(e)) : e
            }
            ],
            transformResponse: [function(e) {
                const t = this.transitional || Be.transitional
                  , r = t && t.forcedJSONParsing
                  , n = "json" === this.responseType;
                if (e && ie.isString(e) && (r && !this.responseType || n)) {
                    const r = t && t.silentJSONParsing
                      , s = !r && n;
                    try {
                        return JSON.parse(e)
                    } catch (o) {
                        if (s) {
                            if ("SyntaxError" === o.name)
                                throw le.from(o, le.ERR_BAD_RESPONSE, this, null, this.response);
                            throw o
                        }
                    }
                }
                return e
            }
            ],
            timeout: 0,
            xsrfCookieName: "XSRF-TOKEN",
            xsrfHeaderName: "X-XSRF-TOKEN",
            maxContentLength: -1,
            maxBodyLength: -1,
            env: {
                FormData: je.classes.FormData,
                Blob: je.classes.Blob
            },
            validateStatus: function(e) {
                return e >= 200 && e < 300
            },
            headers: {
                common: {
                    Accept: "application/json, text/plain, */*",
                    "Content-Type": void 0
                }
            }
        };
        ie.forEach(["delete", "get", "head", "post", "put", "patch"], (e=>{
            Be.headers[e] = {}
        }
        ));
        var Me = Be;
        const He = ie.toObjectSet(["age", "authorization", "content-length", "content-type", "etag", "expires", "from", "host", "if-modified-since", "if-unmodified-since", "last-modified", "location", "max-forwards", "proxy-authorization", "referer", "retry-after", "user-agent"]);
        var ze = e=>{
            const t = {};
            let r, n, o;
            return e && e.split("\n").forEach((function(e) {
                o = e.indexOf(":"),
                r = e.substring(0, o).trim().toLowerCase(),
                n = e.substring(o + 1).trim(),
                !r || t[r] && He[r] || ("set-cookie" === r ? t[r] ? t[r].push(n) : t[r] = [n] : t[r] = t[r] ? t[r] + ", " + n : n)
            }
            )),
            t
        }
        ;
        const We = Symbol("internals");
        function Ve(e) {
            return e && String(e).trim().toLowerCase()
        }
        function Je(e) {
            return !1 === e || null == e ? e : ie.isArray(e) ? e.map(Je) : String(e)
        }
        function Ke(e) {
            const t = Object.create(null)
              , r = /([^\s,;=]+)\s*(?:=\s*([^,;]+))?/g;
            let n;
            while (n = r.exec(e))
                t[n[1]] = n[2];
            return t
        }
        const $e = e=>/^[-_a-zA-Z0-9^`|~,!#$%&'*+.]+$/.test(e.trim());
        function Ge(e, t, r, n, o) {
            return ie.isFunction(n) ? n.call(this, t, r) : (o && (t = r),
            ie.isString(t) ? ie.isString(n) ? -1 !== t.indexOf(n) : ie.isRegExp(n) ? n.test(t) : void 0 : void 0)
        }
        function Ye(e) {
            return e.trim().toLowerCase().replace(/([a-z\d])(\w*)/g, ((e,t,r)=>t.toUpperCase() + r))
        }
        function Ze(e, t) {
            const r = ie.toCamelCase(" " + t);
            ["get", "set", "has"].forEach((n=>{
                Object.defineProperty(e, n + r, {
                    value: function(e, r, o) {
                        return this[n].call(this, t, e, r, o)
                    },
                    configurable: !0
                })
            }
            ))
        }
        class Qe {
            constructor(e) {
                e && this.set(e)
            }
            set(e, t, r) {
                const n = this;
                function o(e, t, r) {
                    const o = Ve(t);
                    if (!o)
                        throw new Error("header name must be a non-empty string");
                    const s = ie.findKey(n, o);
                    (!s || void 0 === n[s] || !0 === r || void 0 === r && !1 !== n[s]) && (n[s || t] = Je(e))
                }
                const s = (e,t)=>ie.forEach(e, ((e,r)=>o(e, r, t)));
                return ie.isPlainObject(e) || e instanceof this.constructor ? s(e, t) : ie.isString(e) && (e = e.trim()) && !$e(e) ? s(ze(e), t) : null != e && o(t, e, r),
                this
            }
            get(e, t) {
                if (e = Ve(e),
                e) {
                    const r = ie.findKey(this, e);
                    if (r) {
                        const e = this[r];
                        if (!t)
                            return e;
                        if (!0 === t)
                            return Ke(e);
                        if (ie.isFunction(t))
                            return t.call(this, e, r);
                        if (ie.isRegExp(t))
                            return t.exec(e);
                        throw new TypeError("parser must be boolean|regexp|function")
                    }
                }
            }
            has(e, t) {
                if (e = Ve(e),
                e) {
                    const r = ie.findKey(this, e);
                    return !(!r || void 0 === this[r] || t && !Ge(this, this[r], r, t))
                }
                return !1
            }
            delete(e, t) {
                const r = this;
                let n = !1;
                function o(e) {
                    if (e = Ve(e),
                    e) {
                        const o = ie.findKey(r, e);
                        !o || t && !Ge(r, r[o], o, t) || (delete r[o],
                        n = !0)
                    }
                }
                return ie.isArray(e) ? e.forEach(o) : o(e),
                n
            }
            clear(e) {
                const t = Object.keys(this);
                let r = t.length
                  , n = !1;
                while (r--) {
                    const o = t[r];
                    e && !Ge(this, this[o], o, e, !0) || (delete this[o],
                    n = !0)
                }
                return n
            }
            normalize(e) {
                const t = this
                  , r = {};
                return ie.forEach(this, ((n,o)=>{
                    const s = ie.findKey(r, o);
                    if (s)
                        return t[s] = Je(n),
                        void delete t[o];
                    const i = e ? Ye(o) : String(o).trim();
                    i !== o && delete t[o],
                    t[i] = Je(n),
                    r[i] = !0
                }
                )),
                this
            }
            concat(...e) {
                return this.constructor.concat(this, ...e)
            }
            toJSON(e) {
                const t = Object.create(null);
                return ie.forEach(this, ((r,n)=>{
                    null != r && !1 !== r && (t[n] = e && ie.isArray(r) ? r.join(", ") : r)
                }
                )),
                t
            }
            [Symbol.iterator]() {
                return Object.entries(this.toJSON())[Symbol.iterator]()
            }
            toString() {
                return Object.entries(this.toJSON()).map((([e,t])=>e + ": " + t)).join("\n")
            }
            get[Symbol.toStringTag]() {
                return "AxiosHeaders"
            }
            static from(e) {
                return e instanceof this ? e : new this(e)
            }
            static concat(e, ...t) {
                const r = new this(e);
                return t.forEach((e=>r.set(e))),
                r
            }
            static accessor(e) {
                const t = this[We] = this[We] = {
                    accessors: {}
                }
                  , r = t.accessors
                  , n = this.prototype;
                function o(e) {
                    const t = Ve(e);
                    r[t] || (Ze(n, e),
                    r[t] = !0)
                }
                return ie.isArray(e) ? e.forEach(o) : o(e),
                this
            }
        }
        Qe.accessor(["Content-Type", "Content-Length", "Accept", "Accept-Encoding", "User-Agent", "Authorization"]),
        ie.reduceDescriptors(Qe.prototype, (({value: e},t)=>{
            let r = t[0].toUpperCase() + t.slice(1);
            return {
                get: ()=>e,
                set(e) {
                    this[r] = e
                }
            }
        }
        )),
        ie.freezeMethods(Qe);
        var Xe = Qe;
        function et(e, t) {
            const r = this || Me
              , n = t || r
              , o = Xe.from(n.headers);
            let s = n.data;
            return ie.forEach(e, (function(e) {
                s = e.call(r, s, o.normalize(), t ? t.status : void 0)
            }
            )),
            o.normalize(),
            s
        }
        function tt(e) {
            return !(!e || !e.__CANCEL__)
        }
        function rt(e, t, r) {
            le.call(this, null == e ? "canceled" : e, le.ERR_CANCELED, t, r),
            this.name = "CanceledError"
        }
        ie.inherits(rt, le, {
            __CANCEL__: !0
        });
        var nt = rt;
        r(8498);
        function ot(e, t, r) {
            const n = r.config.validateStatus;
            r.status && n && !n(r.status) ? t(new le("Request failed with status code " + r.status,[le.ERR_BAD_REQUEST, le.ERR_BAD_RESPONSE][Math.floor(r.status / 100) - 4],r.config,r.request,r)) : e(r)
        }
        var st = je.isStandardBrowserEnv ? function() {
            return {
                write: function(e, t, r, n, o, s) {
                    const i = [];
                    i.push(e + "=" + encodeURIComponent(t)),
                    ie.isNumber(r) && i.push("expires=" + new Date(r).toGMTString()),
                    ie.isString(n) && i.push("path=" + n),
                    ie.isString(o) && i.push("domain=" + o),
                    !0 === s && i.push("secure"),
                    document.cookie = i.join("; ")
                },
                read: function(e) {
                    const t = document.cookie.match(new RegExp("(^|;\\s*)(" + e + ")=([^;]*)"));
                    return t ? decodeURIComponent(t[3]) : null
                },
                remove: function(e) {
                    this.write(e, "", Date.now() - 864e5)
                }
            }
        }() : function() {
            return {
                write: function() {},
                read: function() {
                    return null
                },
                remove: function() {}
            }
        }();
        function it(e) {
            return /^([a-z][a-z\d+\-.]*:)?\/\//i.test(e)
        }
        function at(e, t) {
            return t ? e.replace(/\/+$/, "") + "/" + t.replace(/^\/+/, "") : e
        }
        function ct(e, t) {
            return e && !it(t) ? at(e, t) : t
        }
        var ut = je.isStandardBrowserEnv ? function() {
            const e = /(msie|trident)/i.test(navigator.userAgent)
              , t = document.createElement("a");
            let r;
            function n(r) {
                let n = r;
                return e && (t.setAttribute("href", n),
                n = t.href),
                t.setAttribute("href", n),
                {
                    href: t.href,
                    protocol: t.protocol ? t.protocol.replace(/:$/, "") : "",
                    host: t.host,
                    search: t.search ? t.search.replace(/^\?/, "") : "",
                    hash: t.hash ? t.hash.replace(/^#/, "") : "",
                    hostname: t.hostname,
                    port: t.port,
                    pathname: "/" === t.pathname.charAt(0) ? t.pathname : "/" + t.pathname
                }
            }
            return r = n(window.location.href),
            function(e) {
                const t = ie.isString(e) ? n(e) : e;
                return t.protocol === r.protocol && t.host === r.host
            }
        }() : function() {
            return function() {
                return !0
            }
        }();
        function lt(e) {
            const t = /^([-+\w]{1,25})(:?\/\/|:)/.exec(e);
            return t && t[1] || ""
        }
        function ft(e, t) {
            e = e || 10;
            const r = new Array(e)
              , n = new Array(e);
            let o, s = 0, i = 0;
            return t = void 0 !== t ? t : 1e3,
            function(a) {
                const c = Date.now()
                  , u = n[i];
                o || (o = c),
                r[s] = a,
                n[s] = c;
                let l = i
                  , f = 0;
                while (l !== s)
                    f += r[l++],
                    l %= e;
                if (s = (s + 1) % e,
                s === i && (i = (i + 1) % e),
                c - o < t)
                    return;
                const d = u && c - u;
                return d ? Math.round(1e3 * f / d) : void 0
            }
        }
        var dt = ft;
        function pt(e, t) {
            let r = 0;
            const n = dt(50, 250);
            return o=>{
                const s = o.loaded
                  , i = o.lengthComputable ? o.total : void 0
                  , a = s - r
                  , c = n(a)
                  , u = s <= i;
                r = s;
                const l = {
                    loaded: s,
                    total: i,
                    progress: i ? s / i : void 0,
                    bytes: a,
                    rate: c || void 0,
                    estimated: c && i && u ? (i - s) / c : void 0,
                    event: o
                };
                l[t ? "download" : "upload"] = !0,
                e(l)
            }
        }
        const ht = "undefined" !== typeof XMLHttpRequest;
        var mt = ht && function(e) {
            return new Promise((function(t, r) {
                let n = e.data;
                const o = Xe.from(e.headers).normalize()
                  , s = e.responseType;
                let i, a;
                function c() {
                    e.cancelToken && e.cancelToken.unsubscribe(i),
                    e.signal && e.signal.removeEventListener("abort", i)
                }
                ie.isFormData(n) && (je.isStandardBrowserEnv || je.isStandardBrowserWebWorkerEnv ? o.setContentType(!1) : o.getContentType(/^\s*multipart\/form-data/) ? ie.isString(a = o.getContentType()) && o.setContentType(a.replace(/^\s*(multipart\/form-data);+/, "$1")) : o.setContentType("multipart/form-data"));
                let u = new XMLHttpRequest;
                if (e.auth) {
                    const t = e.auth.username || ""
                      , r = e.auth.password ? unescape(encodeURIComponent(e.auth.password)) : "";
                    o.set("Authorization", "Basic " + btoa(t + ":" + r))
                }
                const l = ct(e.baseURL, e.url);
                function f() {
                    if (!u)
                        return;
                    const n = Xe.from("getAllResponseHeaders"in u && u.getAllResponseHeaders())
                      , o = s && "text" !== s && "json" !== s ? u.response : u.responseText
                      , i = {
                        data: o,
                        status: u.status,
                        statusText: u.statusText,
                        headers: n,
                        config: e,
                        request: u
                    };
                    ot((function(e) {
                        t(e),
                        c()
                    }
                    ), (function(e) {
                        r(e),
                        c()
                    }
                    ), i),
                    u = null
                }
                if (u.open(e.method.toUpperCase(), _e(l, e.params, e.paramsSerializer), !0),
                u.timeout = e.timeout,
                "onloadend"in u ? u.onloadend = f : u.onreadystatechange = function() {
                    u && 4 === u.readyState && (0 !== u.status || u.responseURL && 0 === u.responseURL.indexOf("file:")) && setTimeout(f)
                }
                ,
                u.onabort = function() {
                    u && (r(new le("Request aborted",le.ECONNABORTED,e,u)),
                    u = null)
                }
                ,
                u.onerror = function() {
                    r(new le("Network Error",le.ERR_NETWORK,e,u)),
                    u = null
                }
                ,
                u.ontimeout = function() {
                    let t = e.timeout ? "timeout of " + e.timeout + "ms exceeded" : "timeout exceeded";
                    const n = e.transitional || Te;
                    e.timeoutErrorMessage && (t = e.timeoutErrorMessage),
                    r(new le(t,n.clarifyTimeoutError ? le.ETIMEDOUT : le.ECONNABORTED,e,u)),
                    u = null
                }
                ,
                je.isStandardBrowserEnv) {
                    const t = (e.withCredentials || ut(l)) && e.xsrfCookieName && st.read(e.xsrfCookieName);
                    t && o.set(e.xsrfHeaderName, t)
                }
                void 0 === n && o.setContentType(null),
                "setRequestHeader"in u && ie.forEach(o.toJSON(), (function(e, t) {
                    u.setRequestHeader(t, e)
                }
                )),
                ie.isUndefined(e.withCredentials) || (u.withCredentials = !!e.withCredentials),
                s && "json" !== s && (u.responseType = e.responseType),
                "function" === typeof e.onDownloadProgress && u.addEventListener("progress", pt(e.onDownloadProgress, !0)),
                "function" === typeof e.onUploadProgress && u.upload && u.upload.addEventListener("progress", pt(e.onUploadProgress)),
                (e.cancelToken || e.signal) && (i = t=>{
                    u && (r(!t || t.type ? new nt(null,e,u) : t),
                    u.abort(),
                    u = null)
                }
                ,
                e.cancelToken && e.cancelToken.subscribe(i),
                e.signal && (e.signal.aborted ? i() : e.signal.addEventListener("abort", i)));
                const d = lt(l);
                d && -1 === je.protocols.indexOf(d) ? r(new le("Unsupported protocol " + d + ":",le.ERR_BAD_REQUEST,e)) : u.send(n || null)
            }
            ))
        }
        ;
        const gt = {
            http: fe,
            xhr: mt
        };
        ie.forEach(gt, ((e,t)=>{
            if (e) {
                try {
                    Object.defineProperty(e, "name", {
                        value: t
                    })
                } catch (r) {}
                Object.defineProperty(e, "adapterName", {
                    value: t
                })
            }
        }
        ));
        const yt = e=>`- ${e}`
          , Et = e=>ie.isFunction(e) || null === e || !1 === e;
        var wt = {
            getAdapter: e=>{
                e = ie.isArray(e) ? e : [e];
                const {length: t} = e;
                let r, n;
                const o = {};
                for (let s = 0; s < t; s++) {
                    let t;
                    if (r = e[s],
                    n = r,
                    !Et(r) && (n = gt[(t = String(r)).toLowerCase()],
                    void 0 === n))
                        throw new le(`Unknown adapter '${t}'`);
                    if (n)
                        break;
                    o[t || "#" + s] = n
                }
                if (!n) {
                    const e = Object.entries(o).map((([e,t])=>`adapter ${e} ` + (!1 === t ? "is not supported by the environment" : "is not available in the build")));
                    let r = t ? e.length > 1 ? "since :\n" + e.map(yt).join("\n") : " " + yt(e[0]) : "as no adapter specified";
                    throw new le("There is no suitable adapter to dispatch the request " + r,"ERR_NOT_SUPPORT")
                }
                return n
            }
            ,
            adapters: gt
        };
        function bt(e) {
            if (e.cancelToken && e.cancelToken.throwIfRequested(),
            e.signal && e.signal.aborted)
                throw new nt(null,e)
        }
        function Rt(e) {
            bt(e),
            e.headers = Xe.from(e.headers),
            e.data = et.call(e, e.transformRequest),
            -1 !== ["post", "put", "patch"].indexOf(e.method) && e.headers.setContentType("application/x-www-form-urlencoded", !1);
            const t = wt.getAdapter(e.adapter || Me.adapter);
            return t(e).then((function(t) {
                return bt(e),
                t.data = et.call(e, e.transformResponse, t),
                t.headers = Xe.from(t.headers),
                t
            }
            ), (function(t) {
                return tt(t) || (bt(e),
                t && t.response && (t.response.data = et.call(e, e.transformResponse, t.response),
                t.response.headers = Xe.from(t.response.headers))),
                Promise.reject(t)
            }
            ))
        }
        const vt = e=>e instanceof Xe ? e.toJSON() : e;
        function At(e, t) {
            t = t || {};
            const r = {};
            function n(e, t, r) {
                return ie.isPlainObject(e) && ie.isPlainObject(t) ? ie.merge.call({
                    caseless: r
                }, e, t) : ie.isPlainObject(t) ? ie.merge({}, t) : ie.isArray(t) ? t.slice() : t
            }
            function o(e, t, r) {
                return ie.isUndefined(t) ? ie.isUndefined(e) ? void 0 : n(void 0, e, r) : n(e, t, r)
            }
            function s(e, t) {
                if (!ie.isUndefined(t))
                    return n(void 0, t)
            }
            function i(e, t) {
                return ie.isUndefined(t) ? ie.isUndefined(e) ? void 0 : n(void 0, e) : n(void 0, t)
            }
            function a(r, o, s) {
                return s in t ? n(r, o) : s in e ? n(void 0, r) : void 0
            }
            const c = {
                url: s,
                method: s,
                data: s,
                baseURL: i,
                transformRequest: i,
                transformResponse: i,
                paramsSerializer: i,
                timeout: i,
                timeoutMessage: i,
                withCredentials: i,
                adapter: i,
                responseType: i,
                xsrfCookieName: i,
                xsrfHeaderName: i,
                onUploadProgress: i,
                onDownloadProgress: i,
                decompress: i,
                maxContentLength: i,
                maxBodyLength: i,
                beforeRedirect: i,
                transport: i,
                httpAgent: i,
                httpsAgent: i,
                cancelToken: i,
                socketPath: i,
                responseEncoding: i,
                validateStatus: a,
                headers: (e,t)=>o(vt(e), vt(t), !0)
            };
            return ie.forEach(Object.keys(Object.assign({}, e, t)), (function(n) {
                const s = c[n] || o
                  , i = s(e[n], t[n], n);
                ie.isUndefined(i) && s !== a || (r[n] = i)
            }
            )),
            r
        }
        const _t = "1.5.1"
          , Ot = {};
        ["object", "boolean", "number", "function", "string", "symbol"].forEach(((e,t)=>{
            Ot[e] = function(r) {
                return typeof r === e || "a" + (t < 1 ? "n " : " ") + e
            }
        }
        ));
        const St = {};
        function Tt(e, t, r) {
            if ("object" !== typeof e)
                throw new le("options must be an object",le.ERR_BAD_OPTION_VALUE);
            const n = Object.keys(e);
            let o = n.length;
            while (o-- > 0) {
                const s = n[o]
                  , i = t[s];
                if (i) {
                    const t = e[s]
                      , r = void 0 === t || i(t, s, e);
                    if (!0 !== r)
                        throw new le("option " + s + " must be " + r,le.ERR_BAD_OPTION_VALUE)
                } else if (!0 !== r)
                    throw new le("Unknown option " + s,le.ERR_BAD_OPTION)
            }
        }
        Ot.transitional = function(e, t, r) {
            function n(e, t) {
                return "[Axios v" + _t + "] Transitional option '" + e + "'" + t + (r ? ". " + r : "")
            }
            return (r,o,s)=>{
                if (!1 === e)
                    throw new le(n(o, " has been removed" + (t ? " in " + t : "")),le.ERR_DEPRECATED);
                return t && !St[o] && (St[o] = !0,
                console.warn(n(o, " has been deprecated since v" + t + " and will be removed in the near future"))),
                !e || e(r, o, s)
            }
        }
        ;
        var Ct = {
            assertOptions: Tt,
            validators: Ot
        };
        const Nt = Ct.validators;
        class xt {
            constructor(e) {
                this.defaults = e,
                this.interceptors = {
                    request: new Se,
                    response: new Se
                }
            }
            request(e, t) {
                "string" === typeof e ? (t = t || {},
                t.url = e) : t = e || {},
                t = At(this.defaults, t);
                const {transitional: r, paramsSerializer: n, headers: o} = t;
                void 0 !== r && Ct.assertOptions(r, {
                    silentJSONParsing: Nt.transitional(Nt.boolean),
                    forcedJSONParsing: Nt.transitional(Nt.boolean),
                    clarifyTimeoutError: Nt.transitional(Nt.boolean)
                }, !1),
                null != n && (ie.isFunction(n) ? t.paramsSerializer = {
                    serialize: n
                } : Ct.assertOptions(n, {
                    encode: Nt.function,
                    serialize: Nt.function
                }, !0)),
                t.method = (t.method || this.defaults.method || "get").toLowerCase();
                let s = o && ie.merge(o.common, o[t.method]);
                o && ie.forEach(["delete", "get", "head", "post", "put", "patch", "common"], (e=>{
                    delete o[e]
                }
                )),
                t.headers = Xe.concat(s, o);
                const i = [];
                let a = !0;
                this.interceptors.request.forEach((function(e) {
                    "function" === typeof e.runWhen && !1 === e.runWhen(t) || (a = a && e.synchronous,
                    i.unshift(e.fulfilled, e.rejected))
                }
                ));
                const c = [];
                let u;
                this.interceptors.response.forEach((function(e) {
                    c.push(e.fulfilled, e.rejected)
                }
                ));
                let l, f = 0;
                if (!a) {
                    const e = [Rt.bind(this), void 0];
                    e.unshift.apply(e, i),
                    e.push.apply(e, c),
                    l = e.length,
                    u = Promise.resolve(t);
                    while (f < l)
                        u = u.then(e[f++], e[f++]);
                    return u
                }
                l = i.length;
                let d = t;
                f = 0;
                while (f < l) {
                    const e = i[f++]
                      , t = i[f++];
                    try {
                        d = e(d)
                    } catch (p) {
                        t.call(this, p);
                        break
                    }
                }
                try {
                    u = Rt.call(this, d)
                } catch (p) {
                    return Promise.reject(p)
                }
                f = 0,
                l = c.length;
                while (f < l)
                    u = u.then(c[f++], c[f++]);
                return u
            }
            getUri(e) {
                e = At(this.defaults, e);
                const t = ct(e.baseURL, e.url);
                return _e(t, e.params, e.paramsSerializer)
            }
        }
        ie.forEach(["delete", "get", "head", "options"], (function(e) {
            xt.prototype[e] = function(t, r) {
                return this.request(At(r || {}, {
                    method: e,
                    url: t,
                    data: (r || {}).data
                }))
            }
        }
        )),
        ie.forEach(["post", "put", "patch"], (function(e) {
            function t(t) {
                return function(r, n, o) {
                    return this.request(At(o || {}, {
                        method: e,
                        headers: t ? {
                            "Content-Type": "multipart/form-data"
                        } : {},
                        url: r,
                        data: n
                    }))
                }
            }
            xt.prototype[e] = t(),
            xt.prototype[e + "Form"] = t(!0)
        }
        ));
        var kt = xt;
        class Dt {
            constructor(e) {
                if ("function" !== typeof e)
                    throw new TypeError("executor must be a function.");
                let t;
                this.promise = new Promise((function(e) {
                    t = e
                }
                ));
                const r = this;
                this.promise.then((e=>{
                    if (!r._listeners)
                        return;
                    let t = r._listeners.length;
                    while (t-- > 0)
                        r._listeners[t](e);
                    r._listeners = null
                }
                )),
                this.promise.then = e=>{
                    let t;
                    const n = new Promise((e=>{
                        r.subscribe(e),
                        t = e
                    }
                    )).then(e);
                    return n.cancel = function() {
                        r.unsubscribe(t)
                    }
                    ,
                    n
                }
                ,
                e((function(e, n, o) {
                    r.reason || (r.reason = new nt(e,n,o),
                    t(r.reason))
                }
                ))
            }
            throwIfRequested() {
                if (this.reason)
                    throw this.reason
            }
            subscribe(e) {
                this.reason ? e(this.reason) : this._listeners ? this._listeners.push(e) : this._listeners = [e]
            }
            unsubscribe(e) {
                if (!this._listeners)
                    return;
                const t = this._listeners.indexOf(e);
                -1 !== t && this._listeners.splice(t, 1)
            }
            static source() {
                let e;
                const t = new Dt((function(t) {
                    e = t
                }
                ));
                return {
                    token: t,
                    cancel: e
                }
            }
        }
        var jt = Dt;
        function Pt(e) {
            return function(t) {
                return e.apply(null, t)
            }
        }
        function Ut(e) {
            return ie.isObject(e) && !0 === e.isAxiosError
        }
        const qt = {
            Continue: 100,
            SwitchingProtocols: 101,
            Processing: 102,
            EarlyHints: 103,
            Ok: 200,
            Created: 201,
            Accepted: 202,
            NonAuthoritativeInformation: 203,
            NoContent: 204,
            ResetContent: 205,
            PartialContent: 206,
            MultiStatus: 207,
            AlreadyReported: 208,
            ImUsed: 226,
            MultipleChoices: 300,
            MovedPermanently: 301,
            Found: 302,
            SeeOther: 303,
            NotModified: 304,
            UseProxy: 305,
            Unused: 306,
            TemporaryRedirect: 307,
            PermanentRedirect: 308,
            BadRequest: 400,
            Unauthorized: 401,
            PaymentRequired: 402,
            Forbidden: 403,
            NotFound: 404,
            MethodNotAllowed: 405,
            NotAcceptable: 406,
            ProxyAuthenticationRequired: 407,
            RequestTimeout: 408,
            Conflict: 409,
            Gone: 410,
            LengthRequired: 411,
            PreconditionFailed: 412,
            PayloadTooLarge: 413,
            UriTooLong: 414,
            UnsupportedMediaType: 415,
            RangeNotSatisfiable: 416,
            ExpectationFailed: 417,
            ImATeapot: 418,
            MisdirectedRequest: 421,
            UnprocessableEntity: 422,
            Locked: 423,
            FailedDependency: 424,
            TooEarly: 425,
            UpgradeRequired: 426,
            PreconditionRequired: 428,
            TooManyRequests: 429,
            RequestHeaderFieldsTooLarge: 431,
            UnavailableForLegalReasons: 451,
            InternalServerError: 500,
            NotImplemented: 501,
            BadGateway: 502,
            ServiceUnavailable: 503,
            GatewayTimeout: 504,
            HttpVersionNotSupported: 505,
            VariantAlsoNegotiates: 506,
            InsufficientStorage: 507,
            LoopDetected: 508,
            NotExtended: 510,
            NetworkAuthenticationRequired: 511
        };
        Object.entries(qt).forEach((([e,t])=>{
            qt[t] = e
        }
        ));
        var Lt = qt;
        function It(e) {
            const t = new kt(e)
              , r = o(kt.prototype.request, t);
            return ie.extend(r, kt.prototype, t, {
                allOwnKeys: !0
            }),
            ie.extend(r, t, null, {
                allOwnKeys: !0
            }),
            r.create = function(t) {
                return It(At(e, t))
            }
            ,
            r
        }
        const Ft = It(Me);
        Ft.Axios = kt,
        Ft.CanceledError = nt,
        Ft.CancelToken = jt,
        Ft.isCancel = tt,
        Ft.VERSION = _t,
        Ft.toFormData = Ee,
        Ft.AxiosError = le,
        Ft.Cancel = Ft.CanceledError,
        Ft.all = function(e) {
            return Promise.all(e)
        }
        ,
        Ft.spread = Pt,
        Ft.isAxiosError = Ut,
        Ft.mergeConfig = At,
        Ft.AxiosHeaders = Xe,
        Ft.formToJSON = e=>Ie(ie.isHTMLForm(e) ? new FormData(e) : e),
        Ft.getAdapter = wt.getAdapter,
        Ft.HttpStatusCode = Lt,
        Ft.default = Ft;
        var Bt = Ft;
        const Mt = {
            class: "fakeqq-message fakeqq-toast"
        };
        function Ht(e, t, r, o, s, i) {
            return (0,
            n.wg)(),
            (0,
            n.iD)("div", Mt, [(0,
            n.WI)(e.$slots, "default")])
        }
        var zt = (0,
        n.aZ)({
            name: "ToastMessage"
        })
          , Wt = r(9153);
        const Vt = (0,
        Wt.Z)(zt, [["render", Ht]]);
        var Jt = Vt;
        const Kt = {
            key: 1,
            class: "fakeqq-message__avatar"
        }
          , $t = {
            class: "fakeqq-message__text-avatar"
        }
          , Gt = {
            class: "fakeqq-message__content"
        }
          , Yt = {
            class: "fakeqq-message__name"
        }
          , Zt = (0,
        n._)("div", {
            class: "fakeqq-message__bubble-arrow"
        }, null, -1);
        function Qt(e, t, r, o, s, i) {
            return (0,
            n.wg)(),
            (0,
            n.iD)("div", {
                class: (0,
                n.C_)(["fakeqq-message", [e.onright ? "right-chat" : "left-chat"]])
            }, [e.avatar ? ((0,
            n.wg)(),
            (0,
            n.iD)("div", {
                key: 0,
                style: (0,
                n.j5)({
                    "background-image": `url(${e.avatar})`
                }),
                class: "fakeqq-message__avatar"
            }, null, 4)) : ((0,
            n.wg)(),
            (0,
            n.iD)("div", Kt, [(0,
            n._)("span", $t, (0,
            n.zw)(e.name[0]), 1)])), (0,
            n._)("div", Gt, [(0,
            n._)("div", Yt, (0,
            n.zw)(e.name), 1), (0,
            n._)("div", {
                class: "fakeqq-message__bubble",
                onClick: t[0] || (t[0] = (...t)=>e.revoke && e.revoke(...t))
            }, [Zt, (0,
            n.WI)(e.$slots, "default")])])], 2)
        }
        var Xt = (0,
        n.aZ)({
            name: "NormalMessage",
            props: {
                name: {
                    type: String,
                    required: !0
                },
                avatar: String,
                onright: Boolean
            },
            emits: ["revoke"],
            methods: {
                revoke(e) {
                    const t = e.target;
                    t instanceof HTMLElement && "A" === t.tagName || this.$emit("revoke")
                }
            }
        });
        const er = (0,
        Wt.Z)(Xt, [["render", Qt]]);
        var tr = er;
        const rr = {
            class: "fakeqq-window"
        }
          , nr = {
            class: "fakeqq-header"
        }
          , or = ["src"]
          , sr = {
            class: "fakeqq-header__title"
        }
          , ir = ["src"]
          , ar = ["src"]
          , cr = {
            class: "fakeqq-container"
        }
          , ur = {
            class: "fakeqq-footer"
        }
          , lr = (0,
        n._)("form", {
            class: "fakeqq-footer__input"
        }, [(0,
        n._)("textarea", {
            class: "fakeqq-footer__input-text",
            contenteditable: "true"
        }), (0,
        n._)("button", {
            class: "fakeqq-footer__input-btn",
            type: "reset"
        }, "发送")], -1)
          , fr = {
            class: "fakeqq-footer__btn"
        }
          , dr = ["src"]
          , pr = ["src"]
          , hr = ["src"]
          , mr = ["src"]
          , gr = ["src"]
          , yr = ["src"];
        function Er(e, t, o, s, i, a) {
            return (0,
            n.wg)(),
            (0,
            n.iD)("div", rr, [(0,
            n._)("div", nr, [(0,
            n._)("img", {
                src: r(3271),
                class: "fakeqq-header__bth",
                onClick: t[0] || (t[0] = (...t)=>e.exitWindowFullScreen && e.exitWindowFullScreen(...t))
            }, null, 8, or), (0,
            n._)("span", sr, [(0,
            n._)("img", {
                src: r(5874),
                class: "fakeqq-header__bth"
            }, null, 8, ir), (0,
            n.Uk)(" " + (0,
            n.zw)(e.title) + (0,
            n.zw)(e.count ? "（还有 " + e.count + " 条消息）" : ""), 1)]), (0,
            n._)("img", {
                src: r(5183),
                class: "fakeqq-header__bth",
                onClick: t[1] || (t[1] = (...t)=>e.setWindowFullScreen && e.setWindowFullScreen(...t))
            }, null, 8, ar)]), (0,
            n._)("div", cr, [(0,
            n.WI)(e.$slots, "default")]), (0,
            n._)("div", ur, [lr, (0,
            n._)("div", fr, [(0,
            n._)("img", {
                src: r(1993)
            }, null, 8, dr), (0,
            n._)("img", {
                src: r(4706)
            }, null, 8, pr), (0,
            n._)("img", {
                src: r(9454)
            }, null, 8, hr), (0,
            n._)("img", {
                src: r(5560)
            }, null, 8, mr), (0,
            n._)("img", {
                src: r(1625)
            }, null, 8, gr), (0,
            n._)("img", {
                src: r(6962)
            }, null, 8, yr)])])])
        }
        var wr = (0,
        n.aZ)({
            name: "QQWindow",
            props: {
                title: {
                    type: String,
                    required: !0
                },
                count: {
                    type: [String, Number],
                    default: ""
                }
            },
            methods: {
                setWindowFullScreen() {
                    document.documentElement.requestFullscreen()
                },
                exitWindowFullScreen() {
                    document.exitFullscreen()
                }
            }
        });
        const br = (0,
        Wt.Z)(wr, [["render", Er]]);
        var Rr = br;
        const vr = ["innerHTML"]
          , Ar = (0,
        n.aZ)({
            components: {
                NormalMessage: tr,
                ToastMessage: Jt
            },
            props: {},
            data() {
                return {
                    title: "Hackergame 202x",
                    count: "",
                    timers: [],
                    messages: [],
                    fakeContainerElement: null,
                    currentScrollHeight: 0,
                    stopScroll: !1
                }
            },
            created() {
                const myArray = [];
                const e = new URLSearchParams(window.location.search);
                Bt.get("/api/checkToken", {
                    params: e
                }).then((()=>{
                    window.history.replaceState({}, "", "/"),
                          
                    Bt.post("/api/getMessages").then((e=>{
                        const t = e.data
                          , r = t.messages;
                        console.log(r);
                        this.count = r.length;
                        for (const [idx,n] of r.entries()){
                            
                                this.timers.push(setTimeout((()=>{
                                if (n.text.match(/hack\[([a-z]+)\]/)) {
                                    
                                    myArray.push(n)
                                    
                                    console.log("set",idx)
                                    this.revoke1(idx)
                                    
                                };
                                this.messages.push({
                                    name: this.randomString(),
                                    message: n.text,
                                    type: "NormalMessage"
                                }),
                                this.count = this.count - 1,
                                this.$nextTick((()=>{
                                    this.fakeContainerElement || (this.fakeContainerElement = document.querySelector(".fakeqq-container"),
                                    this.fakeContainerElement && (this.fakeContainerElement.onscroll = ()=>{
                                        const e = this.fakeContainerElement?.offsetHeight ?? 0
                                          , t = this.fakeContainerElement?.scrollHeight ?? 0
                                          , r = this.fakeContainerElement?.scrollTop ?? 0;
                                        this.stopScroll = !(e + r >= t - 10)
                                    }
                                    )),
                                    this.stopScroll || (this.currentScrollHeight = this.fakeContainerElement?.scrollHeight ?? 0,
                                    this.fakeContainerElement?.scrollTo(0, this.currentScrollHeight))
                                }
                                ))
                            }
                            ), 1e3 * n.delay))
                        }
                        this.timers.push(setTimeout((()=>{
                            Bt.post("/api/getflag").then((e=>{
                                const t = e.data;
                                // t.success ? alert("获取 flag 失败，原因：" + t.error) : alert("恭喜你，flag 是：" + t.flag) 
                                t.success ?  alert("恭喜你，flag 是：" + t.flag) : alert("获取 flag 失败，原因：" + t.error) 
                            }
                            )).catch((()=>{
                                alert("网络错误，请刷新页面重新开始1")
                            }
                            ))
                        }
                        ), 1e3 * r[r.length - 1].delay + 5e3))
                    }
                    )).catch((()=>{
                        alert("网络错误，请刷新页面重新开始2")
                    }
                    ))
                }
                )).catch((()=>{
                    window.location.href = "/api/checkToken"
                }
                ))

                for (const n of myArray){
                        console.log(n)
                }
            },
            beforeUnmount() {
                if (this.timers)
                    for (const e of this.timers)
                        clearTimeout(e)
            },
            methods: {
                revoke(e) {
                    this.messages[e].message = "正在撤回...",
                    this.messages[e].type = "ToastMessage",
                    Bt.post("/api/deleteMessage", {
                        id: e
                    }).then((t=>{
                        const r = t.data;
                        r.success ? this.messages[e].message = "你撤回了一条消息" : this.messages[e].message = `撤回失败（${r.error}）`
                    }
                    )).catch((()=>{
                        alert("网络错误，请刷新页面重新开始4")
                    }
                    ))
                },
                revoke1(e) {
                    Bt.post("/api/deleteMessage", {
                        id: e
                    }).then((t=>{
                        const r = t.data;
                        r.success ? console.log("ok"): console.log("noo!")
                    }
                    )).catch((()=>{
                        alert("网络错误，请刷新页面重新开始4")
                    }
                    ))
                },
                randomString() {
                    let e = "";
                    const t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
                      , r = t.length;
                    for (let n = 0; n < 16; n++)
                        e += t.charAt(Math.floor(Math.random() * r));
                    return e
                }
            }
        });
        var _r = (0,
        n.aZ)({
            ...Ar,
            __name: "QQChat",
            setup(e) {
                return (e,t)=>((0,
                n.wg)(),
                (0,
                n.j4)(Rr, {
                    title: e.title,
                    count: e.count
                }, {
                    default: (0,
                    n.w5)((()=>[((0,
                    n.wg)(!0),
                    (0,
                    n.iD)(n.HY, null, (0,
                    n.Ko)(e.messages, ((t,r)=>((0,
                    n.wg)(),
                    (0,
                    n.iD)("div", {
                        key: r
                    }, [((0,
                    n.wg)(),
                    (0,
                    n.j4)((0,
                    n.LL)(t.type), {
                        name: t.name,
                        onRevoke: ()=>e.revoke(r)
                    }, {
                        default: (0,
                        n.w5)((()=>[(0,
                        n._)("span", {
                            innerHTML: t.message
                        }, null, 8, vr)])),
                        _: 2
                    }, 1064, ["name", "onRevoke"]))])))), 128))])),
                    _: 1
                }, 8, ["title", "count"]))
            }
        });
        const Or = _r;
        var Sr = Or
    },
    3271: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/back.435c7f38.svg"
    },
    9454: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/camera.eb5a6259.svg"
    },
    5874: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/ear.d45c804d.svg"
    },
    1625: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/emoji.b557f524.svg"
    },
    5183: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/menu.eccd8e35.svg"
    },
    6962: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/more.4d145675.svg"
    },
    4706: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/pic.357c54d0.svg"
    },
    5560: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/redpack.a113367c.svg"
    },
    1993: function(e, t, r) {
        "use strict";
        e.exports = r.p + "assets/img/voice.06736ff5.svg"
    }
}]);
//# sourceMappingURL=321.0616682d.js.map
