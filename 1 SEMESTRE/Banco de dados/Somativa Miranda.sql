CREATE DATABASE GestaoEstoque2;
USE GestaoEstoque2;

CREATE TABLE Fornecedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(50)
);

CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(50)
);

CREATE TABLE Transportadora (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(50)
);

CREATE TABLE LocalArmazenamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    capacidade_total INT NOT NULL,
    capacidade_utilizada INT NOT NULL
);

CREATE TABLE Produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao TEXT NOT NULL,
    quantidade_estoque INT NOT NULL,
    id_local_armazenamento INT,
    id_fornecedor INT,
    FOREIGN KEY (id_local_armazenamento) REFERENCES LocalArmazenamento(id),
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(id)
);

CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pendente', 'Processando', 'Enviado', 'Entregue') NOT NULL,
    id_cliente INT,
    id_transportadora INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_transportadora) REFERENCES Transportadora(id)
);

CREATE TABLE ProdutoPedido (
    id_pedido INT,
    id_produto INT,
    quantidade INT NOT NULL,
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id),
    FOREIGN KEY (id_produto) REFERENCES Produto(id)
);

CREATE TABLE MovimentacaoEstoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    tipo_movimentacao ENUM('Entrada', 'Saída') NOT NULL,
    quantidade INT NOT NULL,
    data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_produto) REFERENCES Produto(id)
);

CREATE TABLE Inspecao_Qualidade (
    id_inspecao INT AUTO_INCREMENT PRIMARY KEY,
    data_inspecao DATETIME DEFAULT CURRENT_TIMESTAMP,
    resultado_inspecao ENUM('Aprovado', 'Reprovado') NOT NULL,
    id_produto INT NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES Produto(id)
);

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

DELIMITER //
CREATE PROCEDURE RegistrarInspecao(IN produto_id INT, IN resultado ENUM('Aprovado', 'Reprovado'))
BEGIN
    INSERT INTO Inspecao_Qualidade (id_produto, resultado_inspecao) 
    VALUES (produto_id, resultado);
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE AtualizarEstoqueAposInspecao()
BEGIN
    UPDATE Produto 
    SET quantidade_estoque = quantidade_estoque - 1
    WHERE id IN (SELECT id_produto FROM Inspecao_Qualidade WHERE resultado_inspecao = 'Reprovado');
END;
//
DELIMITER ;

INSERT INTO Fornecedor (nome, contato) VALUES
('Tech Supply', 'contato@techsupply.com'),
('Max Components', 'contato@maxcomponents.com');

INSERT INTO Cliente (nome, email, telefone) VALUES
('Carlos Mendes', 'carlos@email.com', '11988887777'),
('Fernanda Lopes', 'fernanda@email.com', '11955554444');

INSERT INTO Transportadora (nome, contato) VALUES
('Fast Delivery', 'fast@delivery.com'),
('Global Freight', 'global@freight.com');

INSERT INTO LocalArmazenamento (nome, capacidade_total, capacidade_utilizada) VALUES
('Centro Distribuição Norte', 1500, 750),
('Depósito Leste', 600, 300);

INSERT INTO Produto (descricao, quantidade_estoque, id_local_armazenamento, id_fornecedor) VALUES
('Monitor 4K', 40, 1, 1),
('SSD NVMe 2TB', 85, 2, 2);

INSERT INTO Pedido (status, id_cliente, id_transportadora) VALUES
('Enviado', 1, 1),
('Pendente', 2, 2);

INSERT INTO ProdutoPedido (id_pedido, id_produto, quantidade) VALUES
(1, 1, 1),
(2, 2, 2);

INSERT INTO MovimentacaoEstoque (id_produto, tipo_movimentacao, quantidade) VALUES
(1, 'Entrada', 15),
(2, 'Saída', 10);

INSERT INTO Inspecao_Qualidade (data_inspecao, resultado_inspecao, id_produto) VALUES
(NOW(), 'Aprovado', 1),
(NOW(), 'Reprovado', 2);
