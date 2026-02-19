CREATE DATABASE GestaoEstoque2;
USE GestaoEstoque2;
-- Fornecedor
CREATE TABLE Fornecedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(50)
);

-- Clientes
CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(50)
);

-- Armazenamento
CREATE TABLE LocalArmazenamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    capacidade_total INT NOT NULL,
    capacidade_utilizada INT NOT NULL
);

-- Produtos
CREATE TABLE Produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao TEXT NOT NULL,
    quantidade_estoque INT NOT NULL,
    id_local_armazenamento INT,
    id_fornecedor INT,
    FOREIGN KEY (id_local_armazenamento) REFERENCES LocalArmazenamento(id),
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(id)
);

-- Pedidos
CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pendente', 'Processando', 'Enviado', 'Entregue') NOT NULL,
    id_cliente INT,
    id_transportadora INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_transportadora) REFERENCES Transportadora(id)
);

-- Transportadora
CREATE TABLE Transportadora (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(50)
);

-- Tabela de Produtos por Pedido
CREATE TABLE ProdutoPedido (
    id_pedido INT,
    id_produto INT,
    quantidade INT NOT NULL,
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id),
    FOREIGN KEY (id_produto) REFERENCES Produto(id)
);
-- Movimentação de Estoque
CREATE TABLE MovimentacaoEstoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    tipo_movimentacao ENUM('Entrada', 'Saída') NOT NULL,
    quantidade INT NOT NULL,
    data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_produto) REFERENCES Produto(id)
);

-- disponibilidade de produtos
SELECT p.nome AS Produto, p.quantidade_estoque AS Estoque, l.nome AS Localizacao
FROM Produto p
JOIN LocalArmazenamento l ON p.id_local_armazenamento = l.id
ORDER BY p.nome;

-- movimentação de estoque
SELECT m.data_movimentacao, p.nome AS Produto, m.tipo_movimentacao, m.quantidade
FROM MovimentacaoEstoque m
JOIN Produto p ON m.id_produto = p.id
ORDER BY m.data_movimentacao DESC;

-- Rentrada e saída 
SELECT p.nome AS Produto, 
       SUM(CASE WHEN m.tipo_movimentacao = 'Entrada' THEN m.quantidade ELSE 0 END) AS TotalEntrada,
       SUM(CASE WHEN m.tipo_movimentacao = 'Saída' THEN m.quantidade ELSE 0 END) AS TotalSaida
FROM MovimentacaoEstoque m
JOIN Produto p ON m.id_produto = p.id
GROUP BY p.nome;

-- atualizar estoque
DELIMITER //
CREATE PROCEDURE AtualizarEstoque(IN produto_id INT, IN tipo_movimentacao ENUM('Entrada', 'Saída'), IN qtd INT)
BEGIN
    IF tipo_movimentacao = 'Entrada' THEN
        UPDATE Produto SET quantidade_estoque = quantidade_estoque + qtd WHERE id = produto_id;
    ELSE
        UPDATE Produto SET quantidade_estoque = quantidade_estoque - qtd WHERE id = produto_id;
    END IF;
END;
//
DELIMITER ;

-- produtos no armazenamento
DELIMITER //
CREATE PROCEDURE AlocarProduto(IN produto_id INT)
BEGIN
    DECLARE local_id INT;
    SELECT id INTO local_id FROM LocalArmazenamento WHERE capacidade_utilizada < capacidade_total LIMIT 1;
    IF local_id IS NOT NULL THEN
        UPDATE Produto SET id_local_armazenamento = local_id WHERE id = produto_id;
        UPDATE LocalArmazenamento SET capacidade_utilizada = capacidade_utilizada + 1 WHERE id = local_id;
    END IF;
END;
//
DELIMITER ;
