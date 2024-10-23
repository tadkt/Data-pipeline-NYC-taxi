#!/bin/bash

cmd=$1

usage() {
    echo "Usage: run.sh <command> <arguments>"
    echo "Available commands:"
    echo "  register_connector          Register a new Kafka connector"
    echo "Available arguments:"
    echo "  [connector config path]     Path to connector config (for register_connector only)"
}

if [[ -z "$cmd" ]]; then
    echo "Error: Missing command"
    usage
    exit 1
fi

case $cmd in
    register_connector)
        if [[ -z "$2" ]]; then
            echo "Error: Missing connector config path"
            usage
            exit 1
        fi
        
        config_path="$2"
        
        if [[ ! -f "$config_path" ]]; then
            echo "Error: Config file '$config_path' does not exist"
            exit 1
        fi
        
        echo "Registering a new connector from '$config_path'"
        curl -i -X POST -H "Accept:application/json" -H 'Content-Type: application/json' http://localhost:8083/connectors -d @"$config_path"
        ;;
    *)
        echo "Error: Unknown command '$cmd'"
        usage
        exit 1
        ;;
esac