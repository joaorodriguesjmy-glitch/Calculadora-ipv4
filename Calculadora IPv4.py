import tkinter as tk
from tkinter import messagebox
import ipaddress

class CalculadoraRedeIPv4:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Sub-redes IPv4")
        master.geometry("420x500")
        master.config(padx=20, pady=20)
        
        # Título
        tk.Label(master, text="Calculadora IPv4 (Hosts & Broadcast)", font=("Arial", 14, "bold")).pack(pady=(0, 15))
        
        # Campo Endereço IP
        tk.Label(master, text="Endereço IP (ex: 192.168.1.10):", font=("Arial", 10)).pack(anchor="w", pady=(5, 0))
        self.entry_ip = tk.Entry(master, font=("Arial", 12), width=30)
        self.entry_ip.pack(pady=5)
        
        # Campo Máscara ou Prefixo CIDR
        tk.Label(master, text="Máscara de Sub-rede ou CIDR (ex: 255.255.255.0 ou 24):", font=("Arial", 10)).pack(anchor="w", pady=(5, 0))
        self.entry_mascara = tk.Entry(master, font=("Arial", 12), width=30)
        self.entry_mascara.pack(pady=5)
        
        # Botão para Calcular
        self.btn_calcular = tk.Button(master, text="Calcular Rede", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=self.calcular_rede)
        self.btn_calcular.pack(fill=tk.X, pady=(15, 15), ipady=5)
        
        # Área de Resultados (usando Text para facilitar a formatação)
        tk.Label(master, text="Resultados:", font=("Arial", 11, "bold")).pack(anchor="w")
        self.txt_resultado = tk.Text(master, font=("Consolas", 11), height=10, width=45, state=tk.DISABLED, bg="#f9f9f9")
        self.txt_resultado.pack(pady=5)

    def calcular_rede(self):
        ip_str = self.entry_ip.get().strip()
        mascara_str = self.entry_mascara.get().strip()
        
        if not ip_str or not mascara_str:
            messagebox.showerror("Erro de Entrada", "Por favor, preencha todos os campos.")
            return

        try:
            # Se o usuário digitou a máscara no formato decimal (ex: 255.255.255.0), convertemos para prefixo CIDR
            if "." in mascara_str:
                rede_str = f"{ip_str}/{mascara_str}"
                rede = ipaddress.ip_network(rede_str, strict=False)
            else:
                # Se digitou apenas o prefixo (ex: 24)
                rede_str = f"{ip_str}/{mascara_str}"
                rede = ipaddress.ip_network(rede_str, strict=False)
            
            # Extraindo as informações da rede utilizando a biblioteca nativa 'ipaddress'
            endereco_rede = rede.network_address
            broadcast = rede.broadcast_address
            mascara_subnet = rede.netmask
            total_ips = rede.num_addresses
            
            # Hosts utilizáveis (Total de IPs menos 2: ID da rede e Broadcast)
            if total_ips > 2:
                hosts_utilizaveis = total_ips - 2
                primeiro_host = list(rede.hosts())[0]
                ultimo_host = list(rede.hosts())[-1]
                faixa_hosts = f"{primeiro_host} até {ultimo_host}"
            else:
                hosts_utilizaveis = 0
                faixa_hosts = "N/A (Rede ponto a ponto ou muito pequena)"

            # Montando o texto do resultado
            resultado = (
                f"Endereço de Rede:   {endereco_rede}\n"
                f"Máscara de Sub-rede: {mascara_subnet}\n"
                f"Endereço Broadcast:  {broadcast}\n"
                f"Total de IPs:        {total_ips}\n"
                f"Hosts Utilizáveis:   {hosts_utilizaveis}\n"
                f"Faixa de Hosts:      \n{faixa_hosts}"
            )
            
            # Exibindo no componente Text
            self.txt_resultado.config(state=tk.NORMAL)
            self.txt_resultado.delete("1.0", tk.END)
            self.txt_resultado.insert(tk.END, resultado)
            self.txt_resultado.config(state=tk.DISABLED)
            
        except ValueError as e:
            messagebox.showerror("Erro de Configuração", f"Valores inválidos:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraRedeIPv4(root)
    root.mainloop()