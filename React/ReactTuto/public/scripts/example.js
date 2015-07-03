// tutorial1-raw.js
var CommentBox = React.createClass({
    loadCommentsFromServer:function(){
        //Ajaxなアプリケーションになると、ファイルシステムにおいているファイルを使うより、むしろWebサーバーを使ってアプリを開発することが必要になってくる
        //ajax…HTTP通信機能を使って、Webページのリロードを伴わずにサーバとXML形式のデータのやり取りを行って処理を進めていく対話型Webアプリケーションの実装形態
        //ここのajaxはjQueryの。でも、これだとGETかPOSTかわかんなくない？GETしてるのか。getJSONでも行けそう（ローカルで取ってくるなら）
        //サーバーを立ちあげなくても、React(view)だけならチェックできる。MCはサーバー立ち上げて
        //ajaxテスト方法は普通にcomments.jsonをindexとおなじ階層に置くだけ。書き換わるのを体験できる
      $.ajax({
          url:this.props.url,
          dataType:'json',
          cache:false,
          success:function(data){
              this.setState({data:data});
          }.bind(this),
          error:function(xhr,status,err){
              console.error(this.props.url,status,err.toString());
          }.bind(this)
      });
    },
    //コメントのリストをリフレッシュするロジック
    handleCommentSubmit:function(comment){
        var comments=this.state.data;
        var newComments=comments.concat([comment]);
        this.setState({data:newComments});
        $.ajax({
           url:this.props.url,
            dataType:'json',
            type:'POST',
            data:comment,
            success:function(data){
                this.setState({data:data});
            }.bind(this),
            error:function(xhr,status,err){
                console.error(this.props.url,status,err.toString());
            }.bind(this)
        });
    },
    //一度だけ実行し、コンポーネントの初期状態をセットアップする
    getInitialState:function(){
        return {data:[]};
    },
    //コンポーネントがレンダリングされた時、Reactによって自動的に呼び出されるメソッド
    //this.setState()の呼び出しで更新する

    componentDidMount:function(){
        this.loadCommentsFromServer();
        setInterval(this.loadCommentsFromServer,this.props.pollInterval);
    },
    //render…最終的にHTMLレンダリングされるReactコンポーネントのツリーを返す
    //state…propsがイミュータブルで変更できないのに対し、stateはthis.setState()によって変更可能でミュータブル。親子の相互作用を実装可能
    //stateのアップデート時に、コンポーネントは自信を再レンダリングする
    render: function() {
        return(
            <div className="commentBox">
                <h1>Comments</h1>
                <CommentList data={this.state.data}/>
                <CommentForm onCommentSubmit={this.handleCommentSubmit}/>
            </div>
        );
    }
});

var CommentList=React.createClass({
    render:function(){
        var commentNodes=this.props.data.map(function(comment){
            return(
                <Comment author={comment.author}>
                    {comment.text}
                </Comment>
            );
        });
        return (
            <div className="commentList">
                {commentNodes}
            </div>
        );
    }
});

var CommentForm=React.createClass({
    handleSubmit:function(e){
        //preventDefault()…フォーム送信のブラウザのデフォルトアクションを防ぐために呼び出す
        e.preventDefault();
        //refs…refが割り当てられたコンポーネントを参照する
        //findDOMNode…ネイティブなブラウザのDOM要素を取得する
        var author=React.findDOMNode(this.refs.author).value.trim();
        var text=React.findDOMNode(this.refs.text).value.trim();
        if(!text||!author){
            return;
        }
        this.props.onCommentSubmit({author:author,text:text});
        React.findDOMNode(this.refs.author).value='';
        React.findDOMNode(this.refs.text).value='';
        return;
    },
    render:function(){
        return (
            //onSubmitハンドラ…イベントハンドラ。送信が確定した時にフォームフィールドをクリアする
            //ref…子コンポーネントに名前を割り当てる
            <form className="commentForm" onSubmit={this.handleSubmit}>
                <input type="text" placeholder="Your name" ref="author"/>
                <input type="text" placeholder="Say something..." ref="text"/>
                <input type="submit" value="Post"/>
            </form>
        );
    }
});

//コメントを定義しておけばそれぞれのコメントに同じコードを使いまわせる（機能は細かく分解する）
var Comment=React.createClass({
    render:function(){
        //props…プロパティ。親コンポーネントから渡されたデータをプロパティとして利用できる。propsを使うとCommentListからCommentに渡されたデータを読むことができ、マークアップをレンダリングできる
        //sanitize…これがなくてtoString()からレンダリングすると、"<p>this is<em>another</em>comment</p>"とかなる。（ブラウザにこう表示される。こうすることでXSSから守っている）
        var rawMarkup = marked(this.props.children.toString(),{sanitize:true});
        return(
            <div className="comment">
                <h2 className="commentAuthor">
                    {this.props.author}
                </h2>
                <span dangerouslySetInnerHTML={{__html:rawMarkup}}></span>
            </div>
        );
    }
});

//var data=[
//    {author:"Pate Hunt",text:"This is one comment"},
//    {author:"Jordan Walke",text:"This is *another* comment"}
//];

React.render(
    <CommentBox url="comments.json" pollInterval={2000}/>,
    document.getElementById('content')
);