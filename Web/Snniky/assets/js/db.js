var db = openDatabase("Skinny", "2.0", "Mybase", 4048);
function criarTable(){
  db.transaction((criar) => {
    criar.executeSql("CREATE TABLE IF NOT EXISTS usuarios (ID INTEGER PRIMARY KEY, nome TEXT, senha TEXT)");
  });

  db.transaction((criar) => {
    criar.executeSql("CREATE TABLE IF NOT EXISTS games (ID INTEGER PRIMARY KEY, nome TEXT, url TEXT, hours TEXT, )");
  });
}

function save(nome, senha){
  db.transaction((armazenar) =>{
      armazenar.executeSql("INSERT INTO usuarios(nome, senha) VALUES(? ,?)", [nome, senha]);
  });
};


function listar(){
  let rows = [];
  db.transaction((listar) =>{
    listar.executeSql("SELECT id, nome, senha FROM usuarios", [], (listar, result) => {
      var lines = result.rows
      for(var i = 0; i<lines.length;i++){
        var obj = {
          id: lines[i].ID,
          nome:lines[i].nome,
          senha:lines[i].senha
        }
        rows.push(obj)
        userDados.push(obj)
      }
      op = rows
      return op;
    });
  });
};

function listarUser(nome){
  let rows = [];
  db.transaction((listar) =>{
    listar.executeSql("SELECT id, nome, senha FROM usuarios WHERE nome = ? ", [nome], (listar, result) => {
      var lines = result.rows
      for(var i = 0; i<lines.length;i++){
        var obj = {
          id: lines[i].ID,
          nome:lines[i].nome,
          senha:lines[i].senha
        }
        rows.push(obj)
        userDados.push(obj)
      }
      op = rows
      return op;
    });
  });
};

function atualizar(id, nome, senha){
  db.transaction((atualizar) =>{
    atualizar.executeSql("UPDATE usuarios SET nome=?, senha=? WHERE id=?", [nome, senha, id]);
  });
};

function deletes(){
  db.transaction((del) =>{
    del.executeSql("DROP TABLE usuarios");
  });
};