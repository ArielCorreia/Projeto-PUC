from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DATE, NUMERIC, SMALLINT, VARCHAR, ForeignKey, INTEGER
from models.estoque import Estoque
from models.produto import Produto
from models.base import Base
from datetime import datetime
from config.DBConnection import * 

class Produto_estoque (Base):
    __tablename__ = 'PRODUTO_ESTOQUE'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Estoque.cd_estoque), nullable=False, primary_key=True) 
    nr_lote: Mapped[str] = mapped_column(VARCHAR(10), nullable=False)
    qt_produtoestoque : Mapped[int] = mapped_column(INTEGER, nullable=False) 
    dt_validade: Mapped[datetime] = mapped_column(DATE, nullable=False)
    dt_produtoestoque: Mapped[datetime] = mapped_column(DATE, nullable=False)

    def consulta_produto_estoque(cd_produto):
        try:
            produto_estoque = session.query(Produto.cd_produto,
                                            Produto.nm_produto,
                                            Produto.ds_produto,
                                            Produto.tp_embalagemproduto,
                                            Produto.vl_produto,
                                            Produto_estoque.qt_produtoestoque).\
                join(Produto, Produto.cd_produto == Produto_estoque.cd_produto).\
                filter(Produto_estoque.cd_produto == cd_produto).\
                first()
            return {"status": "1", "data": produto_estoque, "mensagem": "Produto consultado com sucesso"}
        except:
            return {"status": "0", "data": "", "mensagem": "Erro ao consultar o produto no estoque"}