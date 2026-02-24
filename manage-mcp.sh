#!/bin/bash
# Script de gestion des serveurs MCP pour legal-assistant

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_DIR="$SCRIPT_DIR/mcp-servers"

# Couleurs pour l'output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

function print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

function print_error() {
    echo -e "${RED}✗${NC} $1"
}

function print_info() {
    echo -e "${YELLOW}ℹ${NC} $1"
}

function install_server() {
    local server=$1
    local server_dir="$MCP_DIR/$server"
    
    if [ ! -d "$server_dir" ]; then
        print_error "Le serveur $server n'existe pas dans $server_dir"
        return 1
    fi
    
    print_info "Installation des dépendances pour $server..."
    cd "$server_dir"
    npm install
    
    print_info "Compilation de $server..."
    npm run build
    
    print_success "$server installé et compilé avec succès"
}

function update_server() {
    local server=$1
    local server_dir="$MCP_DIR/$server"
    
    if [ ! -d "$server_dir" ]; then
        print_error "Le serveur $server n'existe pas dans $server_dir"
        return 1
    fi
    
    print_info "Mise à jour de $server depuis Git..."
    cd "$server_dir"
    git pull
    
    install_server "$server"
}

function test_server() {
    local server=$1
    local server_dir="$MCP_DIR/$server"
    local index_js="$server_dir/build/index.js"
    
    if [ ! -f "$index_js" ]; then
        print_error "Le serveur $server n'est pas compilé. Exécutez: $0 install $server"
        return 1
    fi
    
    print_info "Test du serveur $server..."
    if node "$index_js" --help 2>/dev/null || echo ""; then
        print_success "$server semble fonctionnel"
    else
        print_error "Erreur lors du test de $server"
        return 1
    fi
}

function status() {
    echo "=== État des serveurs MCP ==="
    echo
    
    for server in entscheidsuche-mcp onlinekommentar-mcp; do
        local server_dir="$MCP_DIR/$server"
        local index_js="$server_dir/build/index.js"
        
        echo "Serveur: $server"
        
        if [ ! -d "$server_dir" ]; then
            print_error "  Non installé"
        elif [ ! -f "$index_js" ]; then
            print_error "  Installé mais non compilé"
        else
            print_success "  Prêt (compilé)"
            echo "    Fichier: $index_js"
        fi
        echo
    done
}

function show_help() {
    echo "Usage: $0 [commande] [serveur]"
    echo
    echo "Commandes:"
    echo "  install [serveur]  - Installe les dépendances et compile un serveur"
    echo "  update [serveur]   - Met à jour depuis Git et recompile un serveur"
    echo "  test [serveur]     - Teste qu'un serveur est fonctionnel"
    echo "  status             - Affiche l'état de tous les serveurs"
    echo "  install-all        - Installe tous les serveurs"
    echo "  update-all         - Met à jour tous les serveurs"
    echo "  help               - Affiche cette aide"
    echo
    echo "Serveurs disponibles:"
    echo "  - entscheidsuche-mcp"
    echo "  - onlinekommentar-mcp"
    echo
    echo "Exemples:"
    echo "  $0 status"
    echo "  $0 install entscheidsuche-mcp"
    echo "  $0 update-all"
}

# Commande principale
case "${1:-status}" in
    install)
        if [ -z "$2" ]; then
            print_error "Veuillez spécifier un serveur"
            show_help
            exit 1
        fi
        install_server "$2"
        ;;
    
    update)
        if [ -z "$2" ]; then
            print_error "Veuillez spécifier un serveur"
            show_help
            exit 1
        fi
        update_server "$2"
        ;;
    
    test)
        if [ -z "$2" ]; then
            print_error "Veuillez spécifier un serveur"
            show_help
            exit 1
        fi
        test_server "$2"
        ;;
    
    install-all)
        install_server "entscheidsuche-mcp"
        install_server "onlinekommentar-mcp"
        ;;
    
    update-all)
        update_server "entscheidsuche-mcp"
        update_server "onlinekommentar-mcp"
        ;;
    
    status)
        status
        ;;
    
    help|--help|-h)
        show_help
        ;;
    
    *)
        print_error "Commande inconnue: $1"
        show_help
        exit 1
        ;;
esac
